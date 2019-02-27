#!/usr/bin/env python

import pandas as pd

df = pd.read_csv('example_data.txt')
print(df, '\n')

df['mean_2_3'] = df[['value_2', 'value_3']].mean(axis=1)

print(df, '\n')

df_g = df.groupby(['run_id'])

for key, data in df_g:
    print(key)
    print('------')
    print(data.describe())
    print('------')
    print('value_2 mean:', data['value_2'].mean())
    print('value_3 mean:', data['value_3'].mean())
    print('=' * 20)
