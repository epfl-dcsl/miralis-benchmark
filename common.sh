#!/bin/bash

# Todo: Replace the ips here
BOARD_IP="user@128.178.116.143"
MIRALIS_IP="user@128.178.116.99"
PROTECT_PAYLOAD_IP="user@128.178.116.99"

function create_folder_if_not_exists() {
    local folder="$1" 
    if [ ! -d "$folder" ]; then
        echo "Folder '$folder' does not exist. Creating..."
        mkdir "$folder"
    fi
}

function RemoteExec() {
    sshpass -p 'starfive' ssh -oStrictHostKeyChecking=no -p 22 "$1" "cd miralis-benchmark;$2";
}

function setup() {
    create_folder_if_not_exists "results"
}

# 

# Syntax to use the command
# RemoteExec $1 "sudo docker stop \$(sudo docker ps -aq)"

# Import the file

# DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"

# source $DIR/common.sh