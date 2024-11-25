# Install dependencies
sudo apt-get install maven

# Install the sampler
git clone http://github.com/brianfrankcooper/YCSB.git
cd YCSB
mvn -pl site.ycsb:memcached-binding -am clean package


# Run the mcached benchmark
./bin/ycsb load memcached -s -P workloads/workloada -p "memcached.hosts=127.0.0.1" > outputLoad.txt
./bin/ycsb run memcached -s -P workloads/workloada -p "memcached.hosts=127.0.0.1" > benchmark_mcached.txt