#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"


function install_linux() {
    # First delete the repository
    RemoteExec $ADDRESS "rm -rf linux"
    
    # Clone the LInux repository
    RemoteExec $ADDRESS "git clone --depth 1 https://github.com/starfive-tech/linux"
    
    # Navigate to the Linux directory
    (time (RemoteExec $ADDRESS "cd linux && make defconfig && make -j4")) 2>> "results/linux_compilation_$1.txt"
}

clear_stats_entries "linux_compilation_$1"

add_miralis_stat_entry  "linux_compilation_$1"

# Currently we run it a single time
for i in {0..0} 
do
    install_linux $1
done

add_miralis_stat_entry "linux_compilation_$1"
