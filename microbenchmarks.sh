# Update
sudo apt-get update

# Install make
sudo apt-get install make
sudo apt-get install gcc

# CPU Microbenchmark
git clone https://github.com/eembc/coremark-pro

cd coremark-pro
make TARGET=linux64 build
make TARGET=linux64 XCMD='-c4' certify-all > "cpu_benchmark.txt"

# Fileystem Microbenchmark

# Network Microbenchmark
sudo apt install iozone3
iozone -a > "network_benchmark.txt"

