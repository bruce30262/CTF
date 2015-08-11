sc: sc.s
	aarch64-linux-gnu-as -o temp.o sc.s
	aarch64-linux-gnu-objcopy -O binary temp.o sc.o
	rm temp.o
	xxd -i sc.o
csc: sc.c
	aarch64-linux-gnu-gcc -z execstack -o sc sc.c
