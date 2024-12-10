########################
# CPU Microbenchmark
########################

cd coremark-pro
make TARGET=linux64 XCMD='-c4' certify-all
cd ..;