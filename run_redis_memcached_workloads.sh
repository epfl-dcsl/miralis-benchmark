# Run the mcached benchmark
mvn -pl site.ycsb:memcached-binding -am clean package
./bin/ycsb load memcached -s -P workloads/workloada -p "memcached.hosts=127.0.0.1" > /dev/null
./bin/ycsb run memcached -s -P workloads/workloada -p "memcached.hosts=127.0.0.1" > workload_memcached.txt

# Run the redis benchmark
mvn -pl site.ycsb:redis-binding -am clean package
./bin/ycsb load redis -s -P workloads/workloada -p "redis.host=127.0.0.1" -p "redis.port=6379" > /dev/null
./bin/ycsb run redis -s -P workloads/workloada -p "redis.host=127.0.0.1" -p "redis.port=6379" > workload_redis.txt