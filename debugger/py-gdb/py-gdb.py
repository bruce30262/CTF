#!/usr/bin/env python

"""
    script to let user can communicate with gdb using python
    using pwntools

    b("main") # break point, can be symbol(string) or address(integer or long)
    b(0x08048000) 
    run()
    c() # continue
    r.sendline(p64(elf.got['puts'])+".%6$p") # send input
    print x(1, "gx", hex(elf.got['puts'])) # examine address
    print x(30, "gx", "$rsp") # examine register

"""

from pwn import *

ELF_PATH = ""
elf = ELF(ELF_PATH)

r = process(["gdb", ELF_PATH])

def init():
    r.sendline("pset option ansicolor off")
    r.sendline("set prompt (gdb)")

def b(p):
    if isinstance(p, str):
        r.sendlineafter("(gdb)", "b "+ p)
    else:
        r.sendlineafter("(gdb)", "b *" + hex(p))

def run():
    r.sendlineafter("(gdb)","r")

def c():
    r.sendlineafter("(gdb)","c")

def x(size, fmt, addr):
    log.info("examine: " + addr)
    cmd = "x/" + str(size) + fmt + " " + addr
    r.sendlineafter("(gdb)", cmd)
    ret = r.recvuntil("(gdb)")
    r.unrecv("(gdb)")
    return ret

if __name__ == "__main__":

    init()

    r.interactive()
