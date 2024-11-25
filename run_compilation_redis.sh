#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"

function install_redis() {
    # First delete the repository
    RemoteExec $ADDRESS "rm -rf redis"
    
    # Clone the Redis repository
    RemoteExec $ADDRESS "git clone https://github.com/redis/redis"
    
    # Navigate to the Redis directory
    (time (RemoteExec $ADDRESS "cd redis; (make -j$(nproc))")) 2>> "results/redis_compilation_$1.txt"
}

clear_stats_entries "redis_compilation_$1"

add_miralis_stat_entry "redis_compilation_$1"
# Currently we run it a single time
for i in {0..0} 
do
    install_redis $1
done
add_miralis_stat_entry "redis_compilation_$1"
