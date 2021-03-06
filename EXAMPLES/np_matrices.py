#!/usr/bin/env python
import numpy as np

m1 = np.matrix([[ 2,  4,  6],
        [10, 20, 30]])

m2 = np.matrix([[ 1, 15, 7],
        [ 3, 25, 8],
        [ 5, 35, 9]])

print('m1 =>\n', m1)
print()

print('m2 =>\n', m2)
print()

print('m1 * 3 =>\n', m1 * 3)
print()

print('m1 * m2 =>\n', m1 * m2)
print()

print('m1.A.transpose() =>\n', m1.A.transpose())
print()

# print('m1.A.transpose() * m2.A =>\n', m1.A.transpose() * m2.A)

print(m2.shape)

im = np.linalg.inv(m2)

print(im)

