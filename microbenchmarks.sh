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

cd ..

# Fileystem Microbenchmark


git clone https://github.com/keystone-enclave/keystone-iozone
cd keystone-iozone

git clone https://github.com/richfelker/musl-cross-make
cd musl-cross-make
make -j$(nproc) TARGET=riscv64-linux-musl
make install TARGET=riscv64-linux-musl

cd ..
git checkout 1378a4fb920e8177a2293c4600ab494ab51de6b8
# TODO: Do we need permission or a sudo here?
CCRV=musl-cross-make/output/bin/riscv64-linux-musl-gcc make keystone

# Run the benchmark now
iozone -a > "network_benchmark.txt"



# Network Microbenchmark
