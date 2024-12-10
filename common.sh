#!/bin/bash

# Todo: Replace the ips here
BOARD_IP="user@128.178.116.99"
MIRALIS_IP="user@128.178.116.99"
PROTECT_PAYLOAD_IP="user@128.178.116.99"

function RemoteExec() {
    ssh "$1" "cd miralis-benchmark;ls;$2";
}

# -oStrictHostKeyChecking=no -p 22 

# Syntax to use the command
# RemoteExec $1 "sudo docker stop \$(sudo docker ps -aq)"

# Import the file

# DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"

# source $DIR/common.sh