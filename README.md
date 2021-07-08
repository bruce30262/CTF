# CTF tools & some other stuff
## Script
[exp_template.py](https://github.com/bruce30262/CTF/blob/master/script/exp_template.py)  
python script template for CTF pwnable challenges, using [pwntools](https://github.com/Gallopsled/pwntools).  

[armtool.alias](https://github.com/bruce30262/CTF/blob/master/script/armtool.alias)  
alias setting for qemu & ARM toolchain.

[bruceutils.py](https://github.com/bruce30262/CTF/blob/master/script/bruceutils.py)  
Some utilities (ex. pack & unpacking data, socket connection ...) written by me, in case of there is no pwntools to use.  

[brucepwn](https://github.com/bruce30262/CTF/blob/master/script/brucepwn/brucepwn/brucepwn.py)  
Self made utilities for CTF pwn challenges.  

[change_ld.py](https://github.com/bruce30262/CTF/blob/master/script/change_ld.py)  
Simple utility to assign new ld.so of the given binary.

## Debugger
Some config files & tools for the debugger  
  
[gdb](https://github.com/bruce30262/CTF/blob/master/debugger/gdb)  
* Using [pwndbg](https://github.com/pwndbg/pwndbg) as the default GNU debugger.  
* Will detect if gdb-multiarch is needed.

[gef](https://github.com/bruce30262/CTF/blob/master/debugger/gef)  
* [GEF](https://github.com/hugsy/gef) is also a great debugger.  
* Will detect if gdb-multiarch is needed. 

[gdbp](https://github.com/bruce30262/CTF/blob/master/debugger/gdbp)  
* [My own peda](https://github.com/bruce30262/peda).  
* Had used this for pretty long time, however I think it's time to move to a more updated gdb plugin.

### Setting:  
* Put `gdb`, `gef`, `gdbp` in the home directory, all of them must be executable.  
* Add the alias setting in `dbg.alias`.

## Shellcode
 shellcode for `execve("/bin/sh", 0, 0)`.  
 Currently support `x86`, `x64`, `ARM` & `AArch64`.  
 Also [scutils](https://github.com/bruce30262/CTF/tree/master/shellcode/utils) helps me generate shellcode more conveniently.
