#!/usr/bin/env python
import getpass

name = 'Anne'
color = 'red'
value = 27

print(name, color, value)
print(name, color, value, sep='/')

print('name', end="=>")
print(name)

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()

with open('DATA/mary.txt') as mary_in:
    lines = mary_in.readlines()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')


full_name = input("PLease enter your full name? ")
names = full_name.split()
if len(names) < 2:
    full_name = input("Unless you're Cher or DeadMau5? Please enter your full name: ")

password = getpass.getpass("Enter your password:")
