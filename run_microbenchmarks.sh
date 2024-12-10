#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"

source $DIR/common.sh

create_folder_if_not_exists() {
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
    ADDRESS=BOARD_IP
elif [[ "$1" == "miralis" ]]; then
    ADDRESS=MIRALIS_IP
elif [[ "$1" == "protect" ]]; then
    ADDRESS=PROTECT_PAYLOAD_IP
else
    echo "Unknown value: $VALUE"
    exit 1
fi

# Output the result
echo "CurrentIP=$ADDRESS"

create_folder_if_not_exists "results"

########################
# CPU Microbenchmark
########################

function cpu_microbenchmark() {
    echo "Running CPU Microbenchmark [Coremarkpro]"

    cd coremark-pro
    make TARGET=linux64 XCMD='-c4' certify-all > "../results/coremarkpro_$1.txt"
    cd ..;

    echo "Done with CPU microbenchmark"
}



########################
# filesystem Microbenchmark
########################

function fs_microbenchmark() {
    echo "Running filesystem microbenchmark [Filesystem]"

    cd keystone-iozone
    ./iozone -a > "../results/iozone_$1.txt"
    cd ..

    echo "Done with disk microbenchmark"
}



########################
# Network Microbenchmark
########################

function network_microbenchmark() {
    echo "Running network microbenchmark [netperf]"

    cd netperf
    # Start the server 
    netserver
    # Benchmark the server
    echo "TCP microbenchmark"
    netperf -H 127.0.0.1 -t TCP_STREAM  > "../results/netperf_$1_tcp.txt"
    echo "UDP microbenchmark"
    netperf -H 127.0.0.1 -t UDP_STREAM  > "../results/netperf_$1_udp.txt"
    echo "RTT microbenchmark"
    netperf -H 127.0.0.1 -t TCP_RR      > "../results/netperf_$1_rtt.txt"
    cd ..

    echo "Done with network microbenchmark"
}

# Run benchmarks
cpu_microbenchmark $1
fs_microbenchmark $1
network_microbenchmark $1