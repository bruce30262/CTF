# CTF tools & some other stuff
## script
[exp_templete.py](https://github.com/bruce30262/CTF/blob/master/script/exp_templete.py)  
python script templete for CTF pwnable challenges, using [pwntools](https://github.com/Gallopsled/pwntools)  

[armtool.alias](https://github.com/bruce30262/CTF/blob/master/script/armtool.alias)  
alias setting for qemu & ARM toolchain

## debugger
some config files for setting the debugger  
[gdb](https://github.com/bruce30262/CTF/blob/master/debugger/gdb)  
Using [peda](https://github.com/bruce30262/peda) for the default GNU debugger  

[pgdb](https://github.com/bruce30262/CTF/blob/master/debugger/pgdb)  
Using [pwndbg](https://github.com/bruce30262/pwndbg) for tracing C++, ARM & ARM64 binary ( have to install gdb-multiarch first)  
( pwndbg works fine with `set print asm-demangle on`, so I prefer to use pwndbg to trace the C++ binary instead of peda )

Usage:  
* Put `gdb` & `pgdb` in the home directory, both of them must be executable  
* Setting alias
    + `alias gdb="~/gdb"`
    + `alias pgdb="~/pgdb"`

## shellcode
 shellcode for `execve("/bin/sh", 0, 0)`  
 now support `x86`, `x64`, `ARM` & `AArch64`
