# Simple shellcode utility by bruce30262
## Features

* Assemble assembly ( both x86 & x64 , using NASM )  
* Generate shellcode ( including char array, length, hex string )

Usage:  
```
bruce30262@ubuntu:~/CTF-master/shellcode/utils$ ./scutils.rb -h
A simple x86 & x64 shellcode utility by bruce30262
Usage: ./scutils.rb [options] [param]
    -f, --file=val                   the assembly file ( ex. --file=shell.s )
    -a, --asm=val [ 32 or 64 ]       assemble assembly file into x86 or x64 binary
    -o, --out=val                    output binary name after assembling the assembly ( default = a.bin )
    -s, --sc, --shellcode            generate shellcode hex string ( ex. myshellcode = "\xcd\x80" )
    -h, --help                       Display this message

bruce30262@ubuntu:~/CTF-master/shellcode/utils$ ll
total 20
drwxrwxr-x 2 bruce30262 bruce30262 4096 Jan 30 07:07 ./
drwxrwxr-x 7 bruce30262 bruce30262 4096 Jan 30 04:49 ../
-rwxrw-r-- 1 bruce30262 bruce30262  977 Jan 30 07:02 orw64.s*
-rw-rw-r-- 1 bruce30262 bruce30262  184 Jan 30 07:07 README.md
-rwxrwxr-x 1 bruce30262 bruce30262 2241 Jan 30 06:55 scutils.rb*
bruce30262@ubuntu:~/CTF-master/shellcode/utils$ cat /home/ctf/flag
asdfdsfsdfds

bruce30262@ubuntu:~/CTF-master/shellcode/utils$ ./scutils.rb -f orw64.s -a 64 -o orw64.bin
output binary: orw64.bin

bruce30262@ubuntu:~/CTF-master/shellcode/utils$ ./orw64.bin
asdfdsfsdfds

bruce30262@ubuntu:~/CTF-master/shellcode/utils$ ./scutils.rb -f orw64.s -s
unsigned char code_o[] = {
  0xeb, 0x2f, 0x5f, 0x48, 0x31, 0xc0, 0x88, 0x47, 0x0e, 0x48, 0x31, 0xf6,
  0x48, 0x31, 0xd2, 0xb0, 0x02, 0x0f, 0x05, 0x48, 0x89, 0xc7, 0x48, 0x31,
  0xc0, 0x48, 0x83, 0xec, 0x50, 0x54, 0x5e, 0xb2, 0x50, 0x0f, 0x05, 0x48,
  0x89, 0xc2, 0xb0, 0x01, 0x40, 0xb7, 0x01, 0x0f, 0x05, 0xb0, 0x3c, 0x0f,
  0x05, 0xe8, 0xcc, 0xff, 0xff, 0xff, 0x2f, 0x68, 0x6f, 0x6d, 0x65, 0x2f,
  0x63, 0x74, 0x66, 0x2f, 0x66, 0x6c, 0x61, 0x67
};
unsigned int code_o_len = 68;
hex string: "\xeb\x2f\x5f\x48\x31\xc0\x88\x47\x0e\x48\x31\xf6\x48\x31\xd2\xb0\x02\x0f\x05\x48\x89\xc7\x48\x31\xc0\x48\x83\xec\x50\x54\x5e\xb2\x50\x0f\x05\x48\x89\xc2\xb0\x01\x40\xb7\x01\x0f\x05\xb0\x3c\x0f\x05\xe8\xcc\xff\xff\xff\x2f\x68\x6f\x6d\x65\x2f\x63\x74\x66\x2f\x66\x6c\x61\x67"

bruce30262@ubuntu:~/CTF-master/shellcode/utils$

```
