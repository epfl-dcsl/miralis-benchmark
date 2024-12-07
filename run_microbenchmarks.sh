#!/bin/bash
set -e 
set -o pipefail

# Move the previous folder - todo: remove this in the future
cd ..

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
if ! [[ "$1" == "board" || "$1" == "miralis" || "$1" == "prote" ]]; then
    echo "Error: Invalid argument. Allowed values are 'board', 'miralis', or 'prote'."
    exit 1
fi

echo "Benchmark type: $1"

create_folder_if_not_exists "results"
create_folder_if_not_exists "results/coremarkpro"
create_folder_if_not_exists "results/iozone"
create_folder_if_not_exists "results/netperf"

########################
# CPU Microbenchmark
########################

echo "Running CPU Microbenchmark [Coremarkpro]"

cd coremark-pro
make TARGET=linux64 XCMD='-c4' certify-all > "../results/coremarkpro/$1.txt"
cd ..;

echo "Done with CPU microbenchmark"

########################
# filesystem Microbenchmark
########################

echo "Running filesystem microbenchmark [Filesystem]"

cd keystone-iozone
../iozone -a > "../results/iozone/$1.txt"
cd ..

echo "Done with disk microbenchmark"

########################
# Network Microbenchmark
########################

echo "Running network microbenchmark [netperf]"

cd netperf
# Start the server 
netserver
# Benchmark the server
echo "TCP microbenchmark"
netperf -H 127.0.0.1 -t TCP_STREAM  > "../results/netperf/$1_tcp.txt"
echo "UDP microbenchmark"
netperf -H 127.0.0.1 -t UDP_STREAM  > "../results/netperf/$1_udp.txt"
echo "RTT microbenchmark"
netperf -H 127.0.0.1 -t TCP_RR      > "../results/netperf/$1_rtt.txt"
cd ..

echo "Done with network microbenchmark"