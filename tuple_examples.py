#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

junk1 = 'hello'   # string
junk2 = 'hello',  # tuple

print(person, len(person), person[0])

def greet(whom):
    print("Hello,", whom[0])

greet(person)

first_name, last_name, product = person
print(first_name, last_name, '\n')

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
    ('John', 'Strickler'),
    ('Joe', 'Schmoe', 'MyProduct1', 'MyProduct2', 'MyProduct3'),
]

for first_name, last_name, *products in people:
    # first_name, last_name, product = people[0]
    # first_name, last_name, product = people[1]
    # first_name, last_name, product = people[2]
    # ...
    print(first_name, last_name, products)
print()

