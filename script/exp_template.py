#!/usr/bin/env python3

from pwn import *
import subprocess
import sys
import time

# from brucepwn import *

HOST = ""
PORT = 10001
ELF_PATH = ""
LIBC_PATH = ""

context.binary = ELF_PATH
context.log_level = 'INFO' # ['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING']
context.terminal = ['tmux', 'splitw'] # for gdb.attach

elf = context.binary # context.binary is an ELF object
libc = elf.libc if not LIBC_PATH else ELF(LIBC_PATH)
if not libc: log.warning("Failed to load libc")

if __name__ == "__main__":

    # if the binary is run by qemu-static
    # set the signal handler so I can send ctrl-c to qemu-static (interrupt the debbuger)
    if context.arch == "arm" or context.arch == "aarch64":
        signal.signal(signal.SIGINT, sigint_handler)   
    
    #r = remote(HOST, PORT)
    r = elf.process() # elf.process(argv=[argv1, argv2,...])
    #gdb.attach(r, gdbscript=open("./ggg", "r"))

    r.interactive()
