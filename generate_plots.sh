#!/bin/bash
set -e 
set -o pipefail

mkdir -p plots/

echo "Plotting CPU Microbenchmark"
python3 coremark.py

echo "Plotting Disk Microbenchmark"
python3 iozone.py

echo "Plotting Network Microbenchmark"
python3 netperf.py

# echo "Plotting redis and memcached workloads"
# python3 kv_workload.py

# echo "Plotting world switch cost"
# python3 world_switch.py

