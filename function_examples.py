#!/usr/bin/env python
class Spam():
    pass

s = Spam()


def hello():
    print("Hello, world")

def get_message():
    return "Hello, world"

hello()

m = get_message()

print(m)

def greet_person(whom="world"):
    print("Hello,", whom)

greet_person('Mom')

greet_person()

def greet_people1(*person_list):
    for person in person_list:
        print("Hello,", person)

greet_people1("Mom")
print()
greet_people1("Mom", "Dad", "Sis")
print()

def greet_people2(person_list):
    for person in person_list:
        print("Hello,", person)

people = ["Mom", "Dad", "Sis"]
greet_people2(people)
print()
greet_people1(*people)

def process_file(*, file_name, file_type):
    pass

process_file(file_name="foo.hd5",file_type="HDF")
process_file(file_type="CSV", file_name="wombats")

def config(**stuff):
    print(stuff)
    print()

config(animal="wombat", weapon="sock",
       arena="Madison Square Garden")







