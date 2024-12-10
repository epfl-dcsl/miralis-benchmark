
########################
# Network Microbenchmark
########################


cd netperf
# Start the server 
netserver
# Benchmark the server
netperf -H 127.0.0.1 -t TCP_STREAM  > "../results/netperf_$1_tcp.txt"
netperf -H 127.0.0.1 -t UDP_STREAM  > "../results/netperf_$1_udp.txt"
netperf -H 127.0.0.1 -t TCP_RR      > "../results/netperf_$1_rtt.txt"
cd ..

echo "Done with network microbenchmark"