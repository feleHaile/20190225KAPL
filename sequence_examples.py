#!/usr/bin/env python

# [][][][][][] ....

s1 = "foo"
s2 = b'foo'
s3 = ['f', 'o', 'o']
s4 = 'f', 'o', 'o'

print(s1[0])
print(s2[0])
print(s1.encode())
print(s2.decode())

actor = 'John Cena'

print(actor.upper())
print(actor.split())
print(actor[:4])
print(actor[0:4])
print(actor[-1])
print(actor[-4:])

#   S[START:STOP:STEP]

print(actor[::2])
print(actor[1::2])
print(list(zip(actor[::2], actor[1::2])))
print(list(actor))

colors = ['red', 'orange', 'blue']

print(colors, len(colors), colors[-1])
colors.append('pink')
colors.insert(0, 'yellow')
colors.insert(2, 'green')
print(colors)
more_colors = ['black', 'brown', 'tan']

colors.extend(more_colors)
print(colors)

c = colors.pop()
print(c, colors)

c = colors.pop(2)
print(c, colors)

del colors[3]
print(colors)

colors.remove('pink')
print(colors)


