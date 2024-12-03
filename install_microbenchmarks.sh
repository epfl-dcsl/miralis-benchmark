########################
# CPU Microbenchmark
########################

# Update
sudo apt-get update

# Install make
sudo apt-get install make
sudo apt-get install gcc

# CPU Microbenchmark
git clone https://github.com/eembc/coremark-pro

cd coremark-pro
make TARGET=linux64 build
cd ..

########################
# Filesystem Microbenchmark
########################


git clone https://github.com/keystone-enclave/keystone-iozone
cd keystone-iozone

git clone https://github.com/richfelker/musl-cross-make
cd musl-cross-make

make -j$(nproc) TARGET=riscv64-linux-musl
make install TARGET=riscv64-linux-musl

cd ..

git checkout 1378a4fb920e8177a2293c4600ab494ab51de6b8
CCRV=musl-cross-make/output/bin/riscv64-linux-musl-gcc make keystone

cd ..

########################
# Network Microbenchmark
########################

git clone https://github.com/HewlettPackard/netperf/
cd netperf

# Replace confiuration files - files are too old for riscv
rm config.guess
rm config.sug
wget -O config.guess http://git.savannah.gnu.org/cgit/config.git/plain/config.guess
wget -O config.sub http://git.savannah.gnu.org/cgit/config.git/plain/config.sub

# Install
make CFLAGS="-fcommon"
sudo make install

cd ..
