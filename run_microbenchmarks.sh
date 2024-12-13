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

# Run benchmarks
echo "Running CPU Microbenchmark [Coremarkpro]"
RemoteExec $ADDRESS "./microbenchmark_cpu.sh" > "results/coremarkpro_$1.txt"
echo "Done with CPU microbenchmark"

echo "Running filesystem microbenchmark [Filesystem]"
RemoteExec $ADDRESS "./microbenchmark_fs.sh" > "results/iozone_$1.txt"
echo "Done with disk microbenchmark"

echo "Running network microbenchmark [netperf]"

# Start network server
RemoteExec $ADDRESS "./microbenchmark_network.sh $1"

# Launch remote benchmarks
netperf -H $(echo "$ADDRESS" | cut -d'@' -f2-) -t TCP_STREAM  > "results/netperf_$1_tcp.txt"
netperf -H $(echo "$ADDRESS" | cut -d'@' -f2-) -t UDP_STREAM  > "results/netperf_$1_udp.txt"
netperf -H $(echo "$ADDRESS" | cut -d'@' -f2-) -t TCP_RR      > "results/netperf_$1_rtt.txt"

echo "Done with network microbenchmark"

