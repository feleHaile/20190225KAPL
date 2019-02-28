#!/usr/bin/env python

import sys
import ctypes

# <1>
if sys.platform == 'win32':
    fred = ctypes.cdll.LoadLibrary('fred.dll')
elif sys.platform == 'darwin':
    fred = ctypes.cdll.LoadLibrary('fred.dylib')
else:
    fred = ctypes.cdll.LoadLibrary('./fred.so.1.0')

print(dir(fred))  # <2>

print(fred.add(2, 3))  # <3>
print(fred.add(10000, 9999))  # <3>
try:
    print(fred.add(1, []))  # <4>
except Exception as e:
    print("That didn't work...", e)

fred.hello()  # <5>

fred.get_skit.restype = ctypes.c_char_p  # <6>

print(fred.get_skit(1).decode())
print(fred.get_skit(4).decode())
print(fred.get_skit(99).decode())
