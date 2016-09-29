#!/usr/bin/env python

import sys
import os
import re
import struct
import socket
import fcntl
import select
import random
import subprocess
import threading
import telnetlib
import itertools
import time
import signal
import errno
import string
import logging
from datetime import datetime

TIMEOUT = 5
logging.basicConfig(format='\n========== %(levelname)s : %(asctime)s : %(message)s ==========', datefmt='%Y/%m/%d %H:%M:%S')

# pack & unpack
def p8(x):
    return struct.pack('<B', x & 0xff)

def p16(x):
    return struct.pack('<H', x & 0xffff)

def p32(x):
    return struct.pack('<I', x & 0xffffffff)

def p64(x):
    return struct.pack('<Q', x & 0xffffffffffffffff)

def u8(x):
    return struct.unpack('<B', x)[0]

def u16(x):
    return struct.unpack('<H', x.ljust(2, '\x00'))[0]

def u32(x):
    return struct.unpack('<I', x.ljust(4, '\x00'))[0]

def u64(x):
    return struct.unpack('<Q', x.ljust(8, '\x00'))[0]


# socket connection
class RespError(Exception): # raised if the response isn't correct
    def __init__(self, value, expected):
        self.value = value
        self.expected = expected

class SEOFError(Exception): # raised if connection was closed by remote host
    def __init__(self, value):
        self.value = value

class remote: # my own socket class, similar to pwntools
    def __init__(self, host, port):
        self.ip = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.settimeout(TIMEOUT)
        self.sock.connect((host,port))
        
    def send(self, data):
        self.sock.send(data)

    def sendline(self, data):
        self.sock.send(data+"\n")

    def recv(self, num):
        return self.sock.recv(num)
    
    def sendlineafter(self, delim, data):
        resp = self.recvuntil(delim)
        self.sendline(data)
        return resp

    def sendafter(self, delim, data):
        resp = self.recvuntil(delim)
        self.send(data)
        return resp
    
    def recvline(self):
        return self.recvuntil("\n")

    def recvuntil(self, delim):
        try:
            res = ""
            while delim not in res:
                c = self.sock.recv(1)
                if not len(c): # close by remote host
                    raise SEOFError(delim)
                else:
                    res += c
        except socket.timeout as e:
            msg = "Timeout: %s ( port %s )" % (self.ip, self.port)
            logging.exception(msg)
            logerr( "Timeout while recieving: " + repr(delim) )
            logerr( "Recieve result: " + repr(res) )
            self.close()
            sys.exit(-1)
        except SEOFError as e:
            msg = "Connection closed by remote: %s ( port %s )" % (self.ip, self.port)
            logging.exception(msg)
            logerr( "EOF while recieving: " + repr(e.value) )
            logerr( "Recieve result: " + repr(res) )
            self.close()
            sys.exit(-1)
        else:
            return res

    def recvprecise(self, delim):
        resp = self.recvuntil(delim)
        try:
            if resp != delim:
                raise RespError(resp, delim)
        except RespError as e:
            logging.exception(e)
            logerr( "Recieve resp incorrect: " + repr(e.value) )
            logerr( "Expecting: " + repr(e.expected) )
            self.close()
            sys.exit(-1)
        else:   
            return resp

    def interactive(self):
        t = telnetlib.Telnet()
        t.sock = self.sock
        t.interact()
    
    def close(self):
        self.sock.close()

# misc
def myexec(cmd):
    return subprocess.check_output(cmd, shell=True)

def logerr(msg):
    sys.stderr.write(msg+"\n")
    sys.stderr.flush()

def rand_str(upper_bound=10, chars=string.ascii_letters + string.digits):
    size = random.randint(1, upper_bound)
    return ''.join(random.choice(chars) for _ in range(size))
