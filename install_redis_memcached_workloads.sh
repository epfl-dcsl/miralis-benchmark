# Install dependencies
sudo apt-get install maven -y

# Install mcached
sudo apt-get install mcached -y

# Install redis
wget https://download.redis.io/redis-stable.tar.gz
tar -xzvg redis-stable.tar.gz
cd redis-stable 
make 
sudo make install

# Install the sampler
git clone http://github.com/brianfrankcooper/YCSB.git
cd YCSB
# TODO: Continue here