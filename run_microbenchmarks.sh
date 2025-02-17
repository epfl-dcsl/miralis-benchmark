#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"

###############
# Coremark pro
###############

WORKLOAD_NAME="coremarkpro"


# echo "Running CPU Microbenchmark [Coremarkpro]"
# 
# # Clear previous file
# clear_stats_entries "${WORKLOAD_NAME}_$1"
# 
# add_miralis_stat_entry "${WORKLOAD_NAME}_$1"
# RemoteExec $ADDRESS "./microbenchmark_cpu.sh" > "results/${WORKLOAD_NAME}_$1.txt"
# add_miralis_stat_entry "${WORKLOAD_NAME}_$1"
# 
# echo "Done with CPU microbenchmark"

###############
# Iozone
###############

WORKLOAD_NAME="iozone"

echo "Running filesystem microbenchmark [Filesystem]"

# Clear previous file
clear_stats_entries "${WORKLOAD_NAME}_$1"

add_miralis_stat_entry "${WORKLOAD_NAME}_$1"
RemoteExec $ADDRESS "./microbenchmark_fs.sh" > "results/${WORKLOAD_NAME}_$1.txt"
add_miralis_stat_entry "${WORKLOAD_NAME}_$1"

echo "Done with disk microbenchmark"

###############
# Netperf
###############

WORKLOAD_NAME="netperf"

echo "Running network microbenchmark [netperf]"

# Start network server
RemoteExec $ADDRESS "./microbenchmark_network.sh $1"

# Clear previous file
clear_stats_entries "${WORKLOAD_NAME}_$1"

# Launch remote benchmarks
add_miralis_stat_entry "${WORKLOAD_NAME}_$1"
netperf -H $(echo "$ADDRESS" | cut -d'@' -f2-) -t TCP_STREAM -l 30  > "results/${WORKLOAD_NAME}-tcp_$1.txt"
add_miralis_stat_entry "${WORKLOAD_NAME}_$1"
netperf -H $(echo "$ADDRESS" | cut -d'@' -f2-) -t UDP_STREAM -l 30 > "results/${WORKLOAD_NAME}-udp_$1.txt"
add_miralis_stat_entry "${WORKLOAD_NAME}_$1"

echo "Done with network microbenchmark"

