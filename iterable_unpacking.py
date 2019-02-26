#!/usr/bin/env python

values = [1, 2, 3, 4, 5, 6]

a, b, c, d, e, f = values  # iterable unpacking

print(a, b, c, d, e, f)

a, b, *c = values
print(a, b, c)

a, *b, c = values
print(a, b, c)

*a, b, c = values
print(a, b, c)

# for line in my_file:
#     f1, f2, *others = line.split()
