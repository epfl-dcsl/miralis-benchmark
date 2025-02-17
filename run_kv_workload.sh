#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"

[ -d YCSB ] || git clone http://github.com/brianfrankcooper/YCSB.git
cd YCSB

setup "$1"

WORKLOAD_NAME="redis-kv"

# Run the redis benchmark
RemoteExec $ADDRESS "redis-cli CONFIG SET protected-mode no"
./bin/ycsb load redis -s -P workloads/workloada -p "redis.host=$(echo "$ADDRESS" | cut -d'@' -f2-)" -p "redis.port=6379"

clear_stats_entries "${WORKLOAD_NAME}_$1"

add_miralis_stat_entry "${WORKLOAD_NAME}_$1"
./bin/ycsb run redis -s -threads 64 -P workloads/workloada -p operationcount=10000000 -p "redis.host=$(echo "$ADDRESS" | cut -d'@' -f2-)" -p "redis.port=6379" > results/${WORKLOAD_NAME}_$1.txt
add_miralis_stat_entry "${WORKLOAD_NAME}_$1"

WORKLOAD_NAME="memcached-kv"

# # Run the mcached benchmark
# ./bin/ycsb load memcached -s -P workloads/workloada -p "memcached.hosts=$(echo "$ADDRESS" | cut -d'@' -f2-)"
# 
# clear_stats_entries "${WORKLOAD_NAME}_$1"
# 
# add_miralis_stat_entry  "${WORKLOAD_NAME}_$1"
# ./bin/ycsb run memcached -s -threads 64 -P workloads/workloada -p operationcount=10000000 -p "memcached.hosts=$(echo "$ADDRESS" | cut -d'@' -f2-)" > results/${WORKLOAD_NAME}_$1.txt
# add_miralis_stat_entry  "${WORKLOAD_NAME}_$1"

cd ..

cp -r YCSB/results/* results/