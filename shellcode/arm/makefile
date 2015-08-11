sc: sc.s
	arm-linux-gnueabihf-as -o temp.o sc.s
	arm-linux-gnueabihf-objcopy -O binary temp.o sc.o
	rm temp.o
	xxd -i sc.o
csc: sc.c
	arm-linux-gnueabihf-gcc -z execstack -o sc sc.c
