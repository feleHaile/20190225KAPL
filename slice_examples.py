#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]


print(fruits[0], fruits[3], fruits[-1], fruits[-5])
print(fruits[0:5])  # 0, 1, 2, 3, 4
print(fruits[4:9])  # 4, 5, 6, 7, 8
print(fruits[:5])
print(fruits[-5:])
print(fruits[::2], '\n')

print("BEFORE")
print(fruits)
fruits[2:7] = ['grapefruit', 'raspberry', 'plum']
print("AFTER")
print(fruits)
print()
fruits.append('tomato')
fruits.extend(['guava', 'tamarind', 'mangosteen'])
print(fruits)
