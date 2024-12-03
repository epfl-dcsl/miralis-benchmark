# TODO: Run coremark pro remotely

cd coremark-pro
make TARGET=linux64 XCMD='-c4' certify-all > "cpu_benchmark.txt"
cd ..;

# TODO: Run iozone remotely
cd keystone-iozone
iozone -a > "fs_benchmark.txt"
cd ..

# TODO: Run netperf directly from the computer with a remote address
cd netperf
# Start the server 
netserver
# Benchmark the server
netperf -H 127.0.0.1 > "network_benchmark.txt"
cd ..