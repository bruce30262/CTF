#!/bin/bash

set -ex

# use qemu-user to emulate arm enviroment
# will install gcc & g++ toolchain, libc & libstdc++
# download armtool.alias from https://github.com/bruce30262/CTF

APT="apt"

# If nala exist, use nala instead of apt
if command -v nala &> /dev/null
then
    APT="nala"
fi


sudo $APT update

# install g++ if not exist
if ! command -v g++ &> /dev/null
then
    sudo $APT install -y g++
fi

cur_dir=$(dirname $(readlink -f $BASH_SOURCE))
gxx_v=$(g++ -v  2>&1 | tail -1 | awk '{print $3}' | awk -F. '{print $1}')

sudo $APT install -y qemu-user \
    gcc-arm-linux-gnueabihf libc6-dev-armhf-cross gcc-arm-linux-gnueabi libc6-dev-armel-cross \
    gcc-aarch64-linux-gnu libc6-dev-arm64-cross \
    g++-arm-linux-gnueabihf libstdc++-$gxx_v-dev-armhf-cross g++-arm-linux-gnueabi libstdc++-$gxx_v-dev-armel-cross \
    g++-aarch64-linux-gnu libstdc++-$gxx_v-dev-arm64-cross \
    'binfmt*'

set +x
echo "source armtool.alias to apply the latest arm-toolchain setting."
