#!/bin/bash

set -ex

# use qemu-user-static to emulate arm enviroment
# will install gcc & g++ toolchain, libc & libstdc++
# download armtool.alias from https://github.com/bruce30262/CTF

cur_dir=$(dirname $(readlink -f $BASH_SOURCE))
gxx_v=$(g++ -v  2>&1 | tail -1 | awk '{print $3}' | awk -F. '{print $1}')

# qemu-arm-static
sudo apt-get install -y qemu-user-static &&\
# arm (gcc & libc)
sudo apt-get install -y gcc-arm-linux-gnueabihf libc6-dev-armhf-cross gcc-arm-linux-gnueabi libc6-dev-armel-cross &&\
# aarch64 (gcc & libc)
sudo apt-get install -y gcc-aarch64-linux-gnu libc6-dev-arm64-cross &&\
# arm (g++ & libstdc++)
sudo apt-get install -y g++-arm-linux-gnueabihf libstdc++-$gxx_v-dev-armhf-cross g++-arm-linux-gnueabi libstdc++-$gxx_v-dev-armel-cross &&\
# aarch64 (g++ & libstdc++)
sudo apt-get install -y g++-aarch64-linux-gnu libstdc++-$gxx_v-dev-arm64-cross &&\

# binfmt
sudo apt-get install 'binfmt*'

set +x
echo "source armtool.alias to apply the latest arm-toolchain setting."
