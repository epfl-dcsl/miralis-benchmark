#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

function create_folder_if_not_exists() {
    local folder="$1" 
    if [ ! -d "$folder" ]; then
        echo "Folder '$folder' does not exist. Creating..."
        mkdir "$folder"
    fi
}

########################
# Parse input argument
########################

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <arg1>"
    echo "Error: Please provide the benchmark type as argument, options are [board|miralis|protect]"
    exit 1
fi

# We only allow three kind of benchmark types
if ! [[ "$1" == "board" || "$1" == "miralis" || "$1" == "protect" ]]; then
    echo "Error: Invalid argument. Allowed values are 'board', 'miralis', or 'protect'."
    exit 1
fi

echo "Benchmark type: $1"

# Determine ADDRESS based on VALUE
if [[ "$1" == "board" ]]; then
    ADDRESS=$BOARD_IP
elif [[ "$1" == "miralis" ]]; then
    ADDRESS=$MIRALIS_IP
elif [[ "$1" == "protect" ]]; then
    ADDRESS=$PROTECT_PAYLOAD_IP
else
    echo "Unknown value: $VALUE"
    exit 1
fi

# Load the benchmark data
# sysbench \
#     --db-driver=mysql   --mysql-host=$(echo "$ADDRESS" | cut -d'@' -f2-)   --mysql-port=3306 \
#     --mysql-user=user   --mysql-password=user   --mysql-db=sbtest \
#     --tables=10   --table-size=100000   oltp_read_write   prepare

sysbench \
  --db-driver=mysql --mysql-host=$(echo "$ADDRESS" | cut -d'@' -f2-) --mysql-port=3306 \
  --mysql-user=user --mysql-password=user --mysql-db=sbtest \
  --tables=10 --table-size=100000 --threads=8 \
  --time=60 --report-interval=10 oltp_read_write \
  run > "results/mysql_$1.txt"