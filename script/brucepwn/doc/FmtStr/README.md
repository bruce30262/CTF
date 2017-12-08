FmtStr
===================
Simple utility written by me ( bruce30262 )  for constructing format string payload

Idea
-------------
The main purpose of this utility is to help user construct a format string payload that can **write a specific data to a memory address stored at a specific stack position**.

For example we want to construct a format string payload for an x86 ELF : 
```
# first write a single byte to memory address A stored at stack position 10
# then write a single byte to memory address B stored at stack position 11
payload = p32(A) + p32(B)
payload += "%[some number]c" + "%10$hhn"
payload += "%[some number]c" + "%11$hhn"
           ^^^^^^^^^^^^^^^^^
           the most annoying part
```

The utility will focus on helping users **construct "the most annoying part" only** ( which means you'll have to deal with the memory address by yourselves )


Usage
------------
* Create a `FmtStr` object
```python
from brucepwn import *

fmt = FmtStr()
```
* Or you can initialize the object with your own payload
```python
payload = p32(addrA) + p32(addrB)
fmt = FmtStr(payload, printed=8)
# printed: number of already printed bytes
```
* Renew an object
```python
fmt.write(....)
fmt.write(....)
send_payload(fmt)
# now we need a new FmtStr object
fmt.new() # create a new, clean FmtStr object to use. You can also use your own payload, like fmt.new("AAAA", printed=4)
fmt.write(.....)
```

* Write `data` to memory address at stack position `10` with 2 bytes
```python
fmt.write(data=data, index=10, byte=2)
# Or you can use fmt.write(data, 10, 2)
# If you don't want to use index, just pass None: fmt.write(data, None, 2)
``` 

* Use `add_printed` argument to update `printed`
```python
fmt.write(data=data, index=10, byte=2)
fmt.raw("AAAA") # append 4 bytes string "AAAA" to current payload
fmt.write(data=data2, index=11, byte=1, add_printed=4)
```
* Pad a payload string ( useful while constructing the 64 bit format string payload )
```python
fmt.pad(72) # pad to length 72, default character is "A"
# or you can use fmt.pad(72, ch="B") to pad string with "B"
``` 
* Create a payload string for scanning
```python
fmt.scan(10) # will return "%1$p.%2$p.%3$p......%10$p"
fmt.scan(10, start=10) # will return "%10$p.%11$p.%12$p......%19$p"
``` 
* Use `str()` to get the current format string payload
```python
fmt.write(data=data, index=10, byte=2)
fmt.write(data=data2, index=11, byte=1)
fmt.pad(72)
print "fmt payload:{}".format(str(fmt))
# now send the fmt payload
r.sendline(str(fmt))
``` 
 
Example
------------
See [exp.py](https://github.com/bruce30262/CTF/blob/master/script/brucepwn/doc/FmtStr/exp.py) and [exp64.py](https://github.com/bruce30262/CTF/blob/master/script/brucepwn/doc/FmtStr/exp64.py) for the example usage.



