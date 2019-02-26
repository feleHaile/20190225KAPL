#!/usr/bin/env python
# (c)2014 John Strickler
#
from pres import get_info

for term_num in 1, 16, 26, 45:
    print('PRESIDENT {}:'.format(term_num))
    potus_info = get_info(term_num)
    for field, value in potus_info.items():
        print((field, value))
    print()

