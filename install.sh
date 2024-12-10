#!/bin/bash
set -e 
set -o pipefail

########################
# CPU Microbenchmark
########################

# Install dependencies
sudo apt-get install make texinfo gcc g++ xz-utils bzip2 -y

# CPU Microbenchmark
git clone https://github.com/eembc/coremark-pro

cd coremark-pro
make TARGET=linux64 build
cd ..

########################
# Filesystem Microbenchmark
########################


# Installing iozone on the board is really slow:
# Therefore we download the cross compiled program from a remove destination

# TODO: implement this

cd keystone-iozone
wget https://polybox.ethz.ch/index.php/s/MwscmB3UjHHWqa0
cd ..

# git clone https://github.com/keystone-enclave/keystone-iozone
# cd keystone-iozone
# 
# git clone https://github.com/richfelker/musl-cross-make
# cd musl-cross-make
# 
# TARGET=riscv64-linux-musl make -j$(nproc) 
# TARGET=riscv64-linux-musl make install 
# 
# cd ..
# 
# git checkout 1378a4fb920e8177a2293c4600ab494ab51de6b8
# CCRV=musl-cross-make/output/bin/riscv64-linux-musl-gcc make keystone
# 
# cd ..

########################
# Network Microbenchmark
########################

sudo apt install automake autoconf texinfo -y

git clone https://github.com/HewlettPackard/netperf/
cd netperf

# Replace confiuration files - files are too old for riscv
rm config.guess
rm config.sub
wget -O config.guess http://git.savannah.gnu.org/cgit/config.git/plain/config.guess
wget -O config.sub http://git.savannah.gnu.org/cgit/config.git/plain/config.sub

# Install
./autogen.sh
./configure
make CFLAGS="-fcommon"
sudo make install

cd ..

# # Install the ssh client for the experiments
# sudo apt install openssh-server
# sudo systemctl enable ssh
# sudo systemctl start ssh
# sudo ufw allow ssh
# 
# # Install dependencies
# sudo apt-get install maven -y
# 
# # Install mcached
# sudo apt-get install memcached -y
# 
# sudo systemctl start memcached
# sudo systemctl enable memcached
# 
# # Install redis
# wget https://download.redis.io/redis-stable.tar.gz
# tar -xzvf redis-stable.tar.gz
# cd redis-stable 
# make 
# sudo make install
# cd ..
# 
# # Install the sampler
# git clone http://github.com/brianfrankcooper/YCSB.git