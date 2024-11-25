########################
# CPU Microbenchmark
########################

cd coremark-pro
taskset -c 1 make TARGET=linux64 XCMD='-c4' certify-all
cd ..;