#!/usr/bin/env python
import os

print(os.getcwd())
os.chdir('..')
print(os.getcwd())
os.chdir('py3sci3day')
print(os.getcwd())
print(os.getuid())
print(os.getlogin())

print(os.listdir('DATA'), '\n')
xml_files = [f for f in os.listdir('DATA') if f.endswith('.xml')]
print(xml_files, '\n')
print(os.uname())
