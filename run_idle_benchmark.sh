#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"

###############
# Idle benchmark
###############

echo "Running idle benchmark"

# Clear previous file
clear_stats_entries "idle_$1"

add_miralis_stat_entry "idle_$1"
echo "Sleeping 30 seconds"
sleep 10
echo "20 left"
sleep 10
echo "10 left"
sleep 10
add_miralis_stat_entry "idle_$1"

echo "Done with idle benchmark"
