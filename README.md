# CTF tools & some other stuff  

**2023/01/21 Update:** I rarely play CTF now, so some of the tools might be outdated.

## [ctf-tool](https://github.com/bruce30262/CTF/tree/master/ctf-tool)  
Some installation scripts and test files for testing tools.

## [Script](https://github.com/bruce30262/CTF/tree/master/script)
Some useful scripts for CTF pwn challenges.

[exp_template.py](https://github.com/bruce30262/CTF/blob/master/script/exp_template.py)  
python script template for CTF pwnable challenges, using [pwntools](https://github.com/Gallopsled/pwntools).  

[armtool.alias](https://github.com/bruce30262/CTF/blob/master/script/armtool.alias)  
alias setting for qemu & ARM toolchain. See also: [set_arm_env.sh](https://github.com/bruce30262/CTF/blob/master/script/set_arm_env.sh).

[bruceutils.py](https://github.com/bruce30262/CTF/blob/master/script/bruceutils.py)  
Some utilities (ex. pack & unpacking data, socket connection ...) written by me, in case of there is no pwntools to use.  

[brucepwn](https://github.com/bruce30262/CTF/blob/master/script/brucepwn/brucepwn/brucepwn.py)  
Self made utilities for CTF pwn challenges. ( **Written in python2**. Will update when I feel like it :P )  

[change_ld.py](https://github.com/bruce30262/CTF/blob/master/script/change_ld.py)  
Simple utility to assign new ld.so of the given binary.

## [Shellcode](https://github.com/bruce30262/CTF/tree/master/shellcode)
Basic shellcode for `execve("/bin/sh", 0, 0)`. Currently support `x86`, `x64`, `ARM` & `AArch64`.  
Nowadays you might just want to use [pwntools shellcraft](https://docs.pwntools.com/en/stable/shellcraft.html) instead, it's way more convenient.
