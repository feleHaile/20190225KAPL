#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

junk1 = 'hello'   # string
junk2 = 'hello',  # tuple

print(person, len(person), person[0])

def greet(whom):
    print("Hello,", whom[0])

greet(person)

first_name, last_name, product = person
print(first_name, last_name)

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



