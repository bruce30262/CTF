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

if __name__ == "__main__":

    r = remote(HOST, PORT)
    
    r.recvuntil("")
    r.sendline("")

    r.interactive()

