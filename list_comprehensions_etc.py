#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#  [EXPR for VARS in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print("f1: {}\n".format(f1))

SUITS = 'Clubs Diamonds Hearts Spades'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

cards = [f'{r}-{s}' for s in SUITS for r in RANKS]
print("cards:", cards, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2: {}\n".format(f2))

f3 = [f for f in fruits if f.startswith('p')]
print("f3: {}\n".format(f3))

people = [
    ('Melinda', 'Gates', 'Gates Foundation'),
    ('Steve', 'Jobs', 'Apple'),
    ('Larry', 'Wall', 'Perl'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Bill', 'Gates', 'Microsoft'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linus', 'Torvalds', 'Linux'),
]

last_names = [p[0] for p in people if p[0].startswith('L')]
print("last_names: {}".format(last_names))

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [n * 10.0 for n in nums]
print("n1: {}".format(n1))


fgen = (print(f) for f in fruits)
print('-' * 60)
fruits.append('sour cherry')
print(fgen)
for f in fgen:
    print(f)
print("DONE")
for f in fgen:
    print(f)
print("REALLY DONE")

full_names = (f'{f} {l}' for f, l, _ in people)

print(full_names)
for fn in full_names:
    print(fn)


