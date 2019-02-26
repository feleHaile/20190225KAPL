#!/usr/bin/env python

import os

values = (5, 8, 17, 6, 5)
d1 = { v:v**2 for v in values }
print(d1)
print()

DIR = '../DATA/'
files = os.listdir(DIR)
file_sizes = { f:os.path.getsize(DIR + f) for f in files }
for file, size in file_sizes.items():
    print(file, size)

names = ['Matt', 'MATT', 'Mary', 'Fred', 'Wombat', 'Leonard', 'Julie', 'Pam',
         'Fred', 'leonard', 'PAM', 'matt']

unique_names = {n.lower() for n in names}
print(unique_names)

print(set([n.lower() for n in names]))
