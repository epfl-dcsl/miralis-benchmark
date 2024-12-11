########################
# filesystem Microbenchmark
########################

cd keystone-iozone
# Fast one (to run benchmarks faster)
./iozone -s 128k
# Normal one
# ./iozone -a 
cd ..