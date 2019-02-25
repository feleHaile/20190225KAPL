#!/usr/bin/env python

while True:
    name = input("Enter name or q to quit: ")
    if name.strip().lower() == 'q':
        break
    print("Processing {}...".format(name))

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for f in fruits:
    print(f.upper())

target = 'x'
for f in fruits:
    if f.startswith(target):
        print("found", f)
        break
else:
    print("not found")






