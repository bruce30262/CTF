# CTF tools & some other stuff
## script
[exp_templete.py](https://github.com/bruce30262/CTF/blob/master/script/exp_templete.py)  
python script templete for CTF pwnable challenges, using [pwntools](https://github.com/Gallopsled/pwntools)  

[armtool.alias](https://github.com/bruce30262/CTF/blob/master/script/armtool.alias)  
alias setting for qemu & ARM toolchain

[roputils.py](https://github.com/bruce30262/roputils)  
A ROP toolkit, fork from [inaz2](https://github.com/inaz2/roputils)  
I slightly modified some code, so I can do ROP more easily in x64

## debugger
some config files & tools for the debugger  
  
[gdb](https://github.com/bruce30262/CTF/blob/master/debugger/gdb)  
Using [peda](https://github.com/bruce30262/peda) for the default GNU debugger  

[pgdb](https://github.com/bruce30262/CTF/blob/master/debugger/pgdb)  
Using [pwndbg](https://github.com/bruce30262/pwndbg) for tracing ARM & ARM64 binary ( have to install gdb-multiarch first)  

[ga](https://github.com/bruce30262/CTF/blob/master/debugger/ga) & [pga](https://github.com/bruce30262/CTF/blob/master/debugger/pga)  
Script for attaching process  
Usage: `(p)ga [process name]`

##### Setting:  
* Put `gdb`, `pgdb`, `ga` & `pga` in the home directory, all of them must be executable  
* Setting alias
    + `alias gdb="~/gdb"`
    + `alias pgdb="~/pgdb"`
    + `alias ga="~/ga"`
    + `alias pga="~/pga"`
  
[py-gdb](https://github.com/bruce30262/CTF/tree/master/debugger/py-gdb)  
With the help of pwntools, `py-gdb` allow users to communicate with gdb by writing a simple python script.  
Here's an [example](https://github.com/bruce30262/CTF/tree/master/debugger/py-gdb/example)  

## shellcode
 shellcode for `execve("/bin/sh", 0, 0)`  
 now support `x86`, `x64`, `ARM` & `AArch64`  
 Also [scutils](https://github.com/bruce30262/CTF/tree/master/shellcode/utils) helps me generate shellcode more conveniently
