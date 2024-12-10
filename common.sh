#!/bin/bash

# Todo: Replace the ips here
readonly BOARD_IP=Francois@pc841.emulab.net
readonly MIRALIS_IP=Francois@pc790.emulab.net
readonly PROTECT_PAYLOAD_IP=Francois@pc738.emulab.net

function RemoteExec() {
    ssh -oStrictHostKeyChecking=no -p 22 "$1" "$2";
}

# Syntax to use the command
# RemoteExec $1 "sudo docker stop \$(sudo docker ps -aq)"

# Import the file

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"

source $DIR/common.sh