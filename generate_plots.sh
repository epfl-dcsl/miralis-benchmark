#!/bin/bash

mkdir -p plots/

echo "Plotting CPU Microbenchmark"
# python3 coremark.py

echo "Plotting Disk Microbenchmark"
python3 iozone.py

echo "Plotting Network Microbenchmark"
python3 netperf.py

echo "Plotting redis, memcached and mysql workloads"
# python3 databases.py

echo "Plotting compilation time for redis"
python3 redis.py

# echo "Plotting world switch cost"
# python3 world_switch.py

