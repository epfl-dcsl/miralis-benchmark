#!/bin/bash
set -e 
set -o pipefail

# Install dependencies
sudo apt-get install maven -y

# Install mcached
sudo apt-get install memcached -y

sudo systemctl start memcached
sudo systemctl enable memcached

# Install redis
wget https://download.redis.io/redis-stable.tar.gz
tar -xzvf redis-stable.tar.gz
cd redis-stable 
make 
sudo make install
cd ..

# Install the sampler
git clone http://github.com/brianfrankcooper/YCSB.git