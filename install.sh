# Update
sudo apt-get update

# Install make
sudo apt-get install make

# Install coremark-pro
git clone https://github.com/eembc/coremark-pro


# Build and run
cd coremark-pro
make TARGET=linux64 build
make TARGET=linux64 XCMD='-c4' certify-all