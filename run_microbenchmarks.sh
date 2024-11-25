#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"

###############
# Coremark pro
###############

echo "Running CPU Microbenchmark [Coremarkpro]"

# Clear previous file
clear_stats_entries "coremarkpro_$1"

add_miralis_stat_entry "coremarkpro_$1"
RemoteExec $ADDRESS "./microbenchmark_cpu.sh" > "results/coremarkpro_$1.txt"
add_miralis_stat_entry "coremarkpro_$1"

echo "Done with CPU microbenchmark"

###############
# Iozone
###############

echo "Running filesystem microbenchmark [Filesystem]"

# Clear previous file
clear_stats_entries "iozone_$1"

add_miralis_stat_entry "iozone_$1"
RemoteExec $ADDRESS "./microbenchmark_fs.sh" > "results/iozone_$1.txt"
add_miralis_stat_entry "iozone_$1"

echo "Done with disk microbenchmark"

###############
# Netperf
###############

echo "Running network microbenchmark [netperf]"

# Start network server
RemoteExec $ADDRESS "./microbenchmark_network.sh $1"

# Clear previous file
clear_stats_entries "netperf_$1"

# Launch remote benchmarks
add_miralis_stat_entry "netperf_$1"
netperf -H $(echo "$ADDRESS" | cut -d'@' -f2-) -t TCP_STREAM -l 30  > "results/netperf_$1_tcp.txt"
add_miralis_stat_entry "netperf_$1"
netperf -H $(echo "$ADDRESS" | cut -d'@' -f2-) -t UDP_STREAM -l 30 > "results/netperf_$1_udp.txt"
add_miralis_stat_entry "netperf_$1"

echo "Done with network microbenchmark"

