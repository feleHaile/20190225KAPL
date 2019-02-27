#!/usr/bin/env python
from datetime import date, datetime, timedelta, time

today = date.today()
print(today, today.year)

james_bd = date(2014, 8, 1)
print(james_bd)

delta = today - james_bd

print(delta)

years = int(delta.days // 365.25)

print(f"James is {years} years old")

event = datetime(2019, 5, 11, 13, 22, 47)

print(event)

ten_years = timedelta(10 * 365.25)

print(james_bd + ten_years)


import time

start = time.time()
# do something
end = time.time()

seconds = end - start

print("Wait for it....", end="", flush=True)
time.sleep(0)
print("done")

from dateutil.parser import parse
import dateutil.utils

my_dates = [
    "Apr 1, 2019",
    "2019-04-01",
    "4/1/19",
    "4-1-2019",
    "April 1 2019",
    "Feb 31, 2032",
]

for d in my_dates:
    try:
        print(parse(d))
    except Exception as err:
        print(err)


d = dateutil.utils.datetime(2019, 4, 1, 11, 11, 11, 0)

print(d, type(d))


