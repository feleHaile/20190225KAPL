#!/usr/bin/env python
from subprocess import run, PIPE

proc = run("netstat -an", stdout=PIPE, shell=True)

print(proc.returncode)

for line in proc.stdout.decode().splitlines():
    if "ESTABLISHED" in line:
        print(line)

