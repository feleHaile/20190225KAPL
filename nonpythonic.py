#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

for i in range(len(fruits)):
    print(fruits[i])
print()

for fruit in fruits:
    print(fruit)
print()


for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
