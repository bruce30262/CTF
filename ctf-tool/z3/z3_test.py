#!/usr/bin/env python3
from z3 import *
import sys
import binascii

s1 = binascii.unhexlify("703053A1D3703F64B316E4045F3AEE42B1A137156E882AAB")
s2 = binascii.unhexlify("20AC7A25D79CC21D58D01325966ADC7E2EB4B410CB1DC266")

def check(xs, s):
    b = BitVecVal(0, 8)
    for i in range(24):
        a = RotateLeft(xs[i], 3)
        b = RotateRight(b, 2)
        a += b
        a ^= s1[i]
        b = a
        a = RotateLeft(a, 4)
        a ^= s2[i]
        s.add(a == 0)
    
    if s.check() == sat:
        m = s.model()
        a = ""
        for i in range(24):
            a += chr(int(str((m[xs[i]]))))
        print(a)
    else:
        print("unsat")

def solv():
    s = Solver()
    xs = []
    for i in range(24):
        x = BitVec("x%d" % i, 8)
        s.add( 33 <= x )
        s.add( x <= 90 )
        xs.append(x)

    check(xs, s)

solv()
