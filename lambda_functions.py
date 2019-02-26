#!/usr/bin/env python

#                      RETURN VALUE
#  lambda  param-list: expression

def doit(func):
    result = func()
    print(result)

def hello():
    return "HELLO!"

doit(hello)

doit(lambda : "wombats!")


fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

print(sorted(fruits, key=lambda f: f.lower()))




