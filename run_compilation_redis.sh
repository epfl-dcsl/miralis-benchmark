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

function install_redis() {
    # First delete the repository
    RemoteExec $ADDRESS "rm -rf redis"
    
    # Clone the Redis repository
    RemoteExec $ADDRESS "git clone https://github.com/redis/redis"
    
    # Navigate to the Redis directory
    (time (RemoteExec $ADDRESS "cd redis; (make -j$(nproc))")) 2>> "results/redis_compilation_$1.txt"
}

echo "" > "results/redis_compilation_$1.txt"

for i in {0..0} 
do
    install_redis $1
done
