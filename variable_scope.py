#!/usr/bin/env python
from sys import stdout

def print(*bob, **ray):
    stdout.write("HA HA HA! ")
    for arg in bob:
        stdout.write(str(arg).upper() + ray.get('sep', ' '))
    stdout.write(ray.get('end', '\n'))

x = 100  # GLOBAL

len = 12
id = 35
max = 100
min = 50


def spam():
#    x = 5
    y = 42  # LOCAL
    print("x is", x, sep='/')
    print("y is", y, end='\n')


spam()
print("x is", x)
# print("y is", y)
