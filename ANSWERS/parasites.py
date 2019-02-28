#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Jun 15 03:01:05 2013

"""
import pandas as pd

df = pd.read_csv('../DATA/parasite_data.csv')

print(df.head())
print()

df2 = df[df['ShannonDiversity'] >= 1.0]
print(df2.head())
print()

# print(df2.values)

