#!/bin/bash
set -e 
set -o pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null 2>&1 && pwd)"
source $DIR/common.sh

setup "$1"

WORKLOAD_NAME="cornell-box"

###############
# Raytracer - cornell box
###############

function ray_tracer() {
    (time (RemoteExec $ADDRESS "./raytracing.github.io/build/Release/theRestOfYourLife > image.ppm")) 2>> "results/${WORKLOAD_NAME}_$1.txt"
}

echo "Running ray tracer benchmark"

clear_stats_entries "${WORKLOAD_NAME}_$1"

add_miralis_stat_entry "${WORKLOAD_NAME}_$1"
# Currently we run it a single time
for i in {0..0} 
do
    ray_tracer $1
done
add_miralis_stat_entry "${WORKLOAD_NAME}_$1"

echo "Done with ray tracer benchmark"
