#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <arg1>"
    echo "Error: Please give the output name"
    exit 1
fi

function install_redis() {

    # First delete the repository
    rm -rf redis

    # Clone the Redis repository
    # git clone https://github.com/redis/redis > /dev/null

    # Navigate to the Redis directory
    # cd redis

    # Run 'make' and capture its timing and output in 'output.txt'
    (time ls) 2>> "../$1"

    # cd ..
}

echo "" > $1

for i in {0..5} 
do
    install_redis $1
done
