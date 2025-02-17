#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"

WORKLOAD_NAME="mysql"

###############
# MySQL
###############


# We need to load & unload after each experiment to make sure we get clean results
# Load the benchmark data
sysbench \
     --db-driver=mysql   --mysql-host=$(echo "$ADDRESS" | cut -d'@' -f2-)   --mysql-port=3306 \
     --mysql-user=user   --mysql-password=user   --mysql-db=sbtest \
     --tables=1   --table-size=100000   oltp_read_write   prepare

# Clear previous file
clear_stats_entries "${WORKLOAD_NAME}_$1"

add_miralis_stat_entry "${WORKLOAD_NAME}_$1"
sysbench \
  --db-driver=mysql --mysql-host=$(echo "$ADDRESS" | cut -d'@' -f2-) --mysql-port=3306 \
  --mysql-user=user --mysql-password=user --mysql-db=sbtest \
  --tables=1 --table-size=100000 --threads=32 \
  --time=300 --report-interval=20 oltp_read_write \
  run > "results/${WORKLOAD_NAME}_$1.txt"
add_miralis_stat_entry "${WORKLOAD_NAME}_$1"

# Remove the benchmark data
sysbench \
     --db-driver=mysql \
     --mysql-host=$(echo "$ADDRESS" | cut -d'@' -f2-) \
     --mysql-port=3306 \
     --mysql-user=user \
     --mysql-password=user \
     --mysql-db=sbtest \
     --tables=1 \
     oltp_read_write \
     cleanup
