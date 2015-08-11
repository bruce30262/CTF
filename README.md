# CTF tools & some other stuff
## script
[exp_templete.py](https://github.com/bruce30262/CTF/blob/master/script/exp_templete.py)  
python script templete for CTF pwnable challenges, using [pwntools](https://github.com/Gallopsled/pwntools)

## debugger
some config files for setting the debugger  
[gdb](https://github.com/bruce30262/CTF/blob/master/debugger/gdb)  
Using [peda](https://github.com/bruce30262/peda) for the default GNU debugger  

[armgdb](https://github.com/bruce30262/CTF/blob/master/debugger/armgdb)  
Using [pwndbg](https://github.com/zachriggle/pwndbg) for tracing the ARM & ARM64 binary ( have to install gdb-multiarch first)

Usage:  
* Put `gdb` & `armgdb` in the home directory, both of them must be executable  
* Setting alias
    + `alias gdb=~/gdb`
    + `alias armgdb=~/armgdb`

## shellcode
 shellcode for `execve("/bin/sh", 0, 0)`  
 now support `x86`, `x64`, `ARM` & `AArch64`
