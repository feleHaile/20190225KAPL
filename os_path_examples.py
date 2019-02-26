#!/usr/bin/env python
import os
import sys
from datetime import datetime

print(sys.platform)  #  darwin=Mac  win32=Windows linux=Linux  etc
print(os.uname())

FOLDER = 'DATA'
FILENAME = 'mary.txt'

#print(os.sep)

file_path = os.path.join(FOLDER, FILENAME)
print("file_path:", file_path)

print(os.path.dirname(file_path))

my_path = 'spam/ham/eggs/toast.py'
print(os.path.dirname(my_path))

print(os.path.basename(file_path))
print(os.path.basename(my_path))

print(os.path.abspath(file_path))
print(os.path.abspath(my_path))

raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)

# from datetime import datetime
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)

file_size = os.path.getsize(file_path)
print("file size:", file_size)

