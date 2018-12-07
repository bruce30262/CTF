# CTF tools & some other stuff
## script
[exp_template.py](https://github.com/bruce30262/CTF/blob/master/script/exp_template.py)  
python script template for CTF pwnable challenges, using [pwntools](https://github.com/Gallopsled/pwntools)  

[armtool.alias](https://github.com/bruce30262/CTF/blob/master/script/armtool.alias)  
alias setting for qemu & ARM toolchain

[bruceutils.py](https://github.com/bruce30262/CTF/blob/master/script/bruceutils.py)  
Some utilities (ex. pack & unpacking data, socket connection ...) written by me, in case of there is no pwntools to use.  

[brucepwn](https://github.com/bruce30262/CTF/blob/master/script/brucepwn/brucepwn/brucepwn.py)  
Self made utilities for CTF pwn challenges  

[change_ld.py](https://github.com/bruce30262/CTF/blob/master/script/change_ld.py)  
Simple utility to assign new ld.so of the given binary

## debugger
some config files & tools for the debugger  
  
[gdb](https://github.com/bruce30262/CTF/blob/master/debugger/gdb)  
Using [peda](https://github.com/bruce30262/peda) for the default GNU debugger  

[pgdb](https://github.com/bruce30262/CTF/blob/master/debugger/pgdb)  
Using [pwndbg](https://github.com/pwndbg/pwndbg) for tracing ARM & ARM64 binary ( have to install gdb-multiarch first)  

[gef](https://github.com/bruce30262/CTF/blob/master/debugger/gef)  
[GEF](https://github.com/hugsy/gef) is also a great debugger.

##### Setting:  
* Put `gdb`, `pgdb`, `gef` in the home directory, all of them must be executable  
* Add the alias setting in `dbg.alias`

## shellcode
 shellcode for `execve("/bin/sh", 0, 0)`  
 now support `x86`, `x64`, `ARM` & `AArch64`  
 Also [scutils](https://github.com/bruce30262/CTF/tree/master/shellcode/utils) helps me generate shellcode more conveniently
