# Install dependencies
sudo apt-get install maven

# Install mcached
sudo apt-get install mcached

# Install redis
wget https://download.redis.io/redis-stable.tar.gz
tar -xzvg redis-stable.tar.gz
cd redis-stable 
make 
sudo make install

# Install the sampler
git clone http://github.com/brianfrankcooper/YCSB.git
cd YCSB

# Run the mcached benchmark
mvn -pl site.ycsb:memcached-binding -am clean package
./bin/ycsb load memcached -s -P workloads/workloada -p "memcached.hosts=127.0.0.1" > outputLoad.txt
./bin/ycsb run memcached -s -P workloads/workloada -p "memcached.hosts=127.0.0.1" > benchmark_mcached.txt

# Run the redis benchmark
mvn -pl site.ycsb:redis-binding -am clean package
./bin/ycsb load redis -s -P workloads/workloada -p "redis.host=127.0.0.1" -p "redis.port=6379" > outputLoad.txt
./bin/ycsb run redis -s -P workloads/workloada -p "redis.host=127.0.0.1" -p "redis.port=6379" > benchmark_redis.txt