#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manticore import Manticore
import subprocess
import sys
import ctypes

def myexec(cmd):
    return subprocess.check_output(cmd, shell=True)

resp = myexec("objdump -M intel -D ./tmp | grep \"400837\"").split("rbp-")[1].strip()[:-1:]
buf1_off = int(resp, 16) 

m = Manticore('./tmp')

# hook strlen
@m.hook(0x400640)
def strlen_model(state):
    buf = state.cpu.read_register('RDI')
    cnt = 0
    while True:
        c = state.cpu.read_int(buf+cnt, 8)
        if c == 0:
            break
        else:
            cnt += 1
    state.cpu.RAX = cnt
    state.cpu.RIP = 0x4009ab # ret gadget

# hook sleep
@m.hook(0x4006c0)
def hook(state):
    state.cpu.RIP = 0x4009ab # ret gadget
# hook puts
@m.hook(0x400630)
def hook(state):
    state.cpu.RIP = 0x4009ab # ret gadget
# hook printf
@m.hook(0x400650)
def hook(state):
    state.cpu.RIP = 0x4009ab # ret gadget
# hook setvbuf
@m.hook(0x400690)
def hook(state):
    state.cpu.RIP = 0x4009ab # ret gadget

# hook read
@m.hook(0x40084b)
def hook(state):
    global buf1_off
    buf = state.cpu.read_register('RSI')
    v = state.new_symbolic_value(32)
    state.cpu.write_int(buf + buf1_off - 0x1c, v, 32)
    state.cpu.RIP = 0x400862 # skip atoi

# wrong branch
@m.hook(0x40088a)
def hook(state):
    print "In wrong branch"
    state.abandon()

ans = dict()
# hook cmp, cal answer
@m.hook(0x400885)
def hook(state):
    global ans
    rbp = state.cpu.read_register('RBP')
    buf = rbp - 0x1c
    num = state.cpu.read_int(buf,32)
    state.constrain(num == state.cpu.RAX)
    for symbol in state.input_symbols:
        if "val_" in symbol.name and (symbol.name not in ans):
            ch =  state._solver.get_value(state.constraints, symbol)
            ch = ctypes.c_int32(ch).value
            #print "{} : {}".format(symbol.name, ch)
            state.cpu.write_int(buf,ch,32)
            ans[symbol.name] = ch

# solve all sums, print answer
@m.hook(0x4008fb)
def hook(state):
    global ans
    print "DILDO!!"
    for i in xrange(2, 22): # val_2 ~ val_21
        key = "val_{}".format(i)
        print ans[key]
    print "DILDO!!"
    m.terminate()

# hook _start
@m.hook(0x4006e0)
def hook(state):
    state.cpu.RIP = 0x400b48

Manticore.verbosity(2)
m.run(procs=10)
