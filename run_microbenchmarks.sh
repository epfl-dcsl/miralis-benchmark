#!/bin/bash

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

cho "Running filesystem microbenchmark [Filesystem]"

cd keystone-iozone
./iozone -a > "../results/iozone/$1.txt"
cd ..

echo "Done with disk microbenchmark"

########################
# Network Microbenchmark
########################

cho "Running network microbenchmark [netperf]"

cd netperf
# Start the server 
netserver
# Benchmark the server
netperf -H 127.0.0.1 -t TCP_STREAM  > "results/netperf/$1\_tcp.txt"
netperf -H 127.0.0.1 -t UDP_STREAM  > "results/netperf/$1\_udp.txt"
netperf -H 127.0.0.1 -t TCP_RR      > "results/netperf/$1\_rtt.txt"
cd ..

echo "Done with network microbenchmark"