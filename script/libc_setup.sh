#!/bin/bash
# from https://github.com/mehQQ/linux_setup/blob/master/libc_setup.sh
mkdir -p $HOME/src
cd $HOME/src
# 64
wget "http://ftp.gnu.org/gnu/glibc/glibc-$1.tar.gz"
tar xvf "glibc-$1.tar.gz"
mkdir -p "$HOME/build/glibc-$1"
cd "$HOME/build/glibc-$1"
CFLAGS="-g -g3 -ggdb -gdwarf-4 -Og -Wno-error=maybe-uninitialized" \
    CXXFLAGS="-g -g3 -ggdb -gdwarf-4 -Og -Wno-error=maybe-uninitialized" \
    "$HOME/src/glibc-$1/configure" --prefix=/usr 
make
# 32
mkdir -p "$HOME/build/glibc32-$1"
cd "$HOME/build/glibc32-$1"
CC="gcc -m32" CXX="g++ -m32" \
    CFLAGS="-g -g3 -ggdb -gdwarf-4 -Og -Wno-error=maybe-uninitialized" \
    CXXFLAGS="-g -g3 -ggdb -gdwarf-4 -Og -Wno-error=maybe-uninitialized" \
    "$HOME/src/glibc-$1/configure" --prefix=/usr \
    --host=i686-linux-gnu 
make
