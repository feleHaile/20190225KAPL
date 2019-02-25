#!/usr/bin/env python

for b in dir(__builtins__):
    if not b.startswith('__'):
        print(b)
