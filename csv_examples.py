#!/usr/bin/env python
import csv

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for row in rdr:
        term, first_name, last_name, birthplace, birth_state, party = row
        term = int(term)
        print(last_name, party)

print('-' * 60)

with open('DATA/presidents.tsv') as pres_in:
    rdr = csv.reader(pres_in, delimiter='\t')
    for row in rdr:
        print(row)

print('-' * 60)

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitinfo.csv', 'w') as fruitinfo_out:
    wtr = csv.writer(fruitinfo_out, quoting=csv.QUOTE_ALL)
    for fruit in fruits:
        data = [fruit[0].upper(), fruit, len(fruit)]
        wtr.writerow(data)

