#!/bin/bash

rm overhead.txt
touch overhead.txt

mkdir -p plots/

echo "Plotting CPU Microbenchmark"
python3 coremark.py
 
echo "Plotting Disk Microbenchmark"
python3 iozone.py

echo "Plotting Network Microbenchmark"
python3 netperf.py

echo "Plotting redis, memcached and mysql workloads"
python3 databases.py

echo "Plotting compilation time for redis"
python3 compilation.py

python3 parse_miralis_info.py

python3 stats.py

# echo "Generating boot"
# python3 boot.py
