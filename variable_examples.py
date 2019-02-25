#!/usr/bin/env python

x = 5
print(x)

y = x

things = [1, 2, 3]
t = things
print(t)
t.append(42)
print(things)
print(t is things)
print(id(t), id(things))

print(type(x), type(t), type(type), type('spam'))

t = 42
print(type(t))
t = "amazon"
print(type(t))

m = None
print(m)

