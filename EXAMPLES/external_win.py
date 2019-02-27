#!/usr/bin/python3

import sys
import os

if sys.platform != 'win32':
    print("This script only runs on Windows")
    sys.exit(1)

# just launch a command
return_code = os.system('ipconfig')
print(return_code)
# open a command and read its output
with os.popen(r'dir ..\DATA') as d:

    for entry in d:
        print(entry, end=' ')

# backticks (``)  equiv
hostname = os.popen('hostname').read()[:-1]

print('Hostname is', hostname)


