#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup

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


[ -d YCSB ] || git clone http://github.com/brianfrankcooper/YCSB.git
cd YCSB

# Run the mcached benchmark
# ./bin/ycsb load memcached -s -P workloads/workloada -p "memcached.hosts=128.178.116.143" > /dev/null
./bin/ycsb run memcached -s -P workloads/workloada -p "memcached.hosts=128.178.116.143" > ../results/workload_memcached_$1.txt

# Run the redis benchmark
# ./bin/ycsb load redis -s -P workloads/workloada -p "redis.host=128.178.116.143" -p "redis.port=6379" > /dev/null
./bin/ycsb run redis -s -P workloads/workloada -p "redis.host=128.178.116.143" -p "redis.port=6379" > ../results/workload_redis_$1.txt

cd ..
