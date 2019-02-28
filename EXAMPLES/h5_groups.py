#!/usr/bin/env python
# (c) 2017 John Strickler
#
from h5py import File

H5_FILE = '../DATA/h5/hdf5_test.h5'

hfile = File(H5_FILE)

print('groups:')
for group in hfile:
    print(group)
print()

print('datasets in /arrays:')
for dataset in hfile['arrays']:
    print(dataset)

