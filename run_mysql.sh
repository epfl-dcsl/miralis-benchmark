#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"

# We need to load & unload after each experiment to make sure we get clean results
# Load the benchmark data
sysbench \
     --db-driver=mysql   --mysql-host=$(echo "$ADDRESS" | cut -d'@' -f2-)   --mysql-port=3306 \
     --mysql-user=user   --mysql-password=user   --mysql-db=sbtest \
     --tables=10   --table-size=100000   oltp_read_write   prepare

# Clear previous file
clear_stats_entries "mysql_$1"

add_miralis_stat_entry "mysql_$1"
sysbench \
  --db-driver=mysql --mysql-host=$(echo "$ADDRESS" | cut -d'@' -f2-) --mysql-port=3306 \
  --mysql-user=user --mysql-password=user --mysql-db=sbtest \
  --tables=10 --table-size=100000 --threads=8 \
  --time=300 --report-interval=10 oltp_read_write \
  run > "results/mysql_$1.txt"
add_miralis_stat_entry "mysql_$1"

# Remove the benchmark data
sysbench \
     --db-driver=mysql \
     --mysql-host=$(echo "$ADDRESS" | cut -d'@' -f2-) \
     --mysql-port=3306 \
     --mysql-user=user \
     --mysql-password=user \
     --mysql-db=sbtest \
     --tables=10 \
     oltp_read_write \
     cleanup
