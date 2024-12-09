#!/bin/bash

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

function install_redis() {

    # First delete the repository
    rm -rf redis

    # Clone the Redis repository
    git clone https://github.com/redis/redis > /dev/null

    # Navigate to the Redis directory
    cd redis

    # Run 'make' and capture its timing and output in 'output.txt'
    (make) 2>> "../results/redis_compilation_$1.txt"

    cd ..
}

echo "" > "results/redis_compilation_$1.txt"

for i in {0..5} 
do
    install_redis $1
done
