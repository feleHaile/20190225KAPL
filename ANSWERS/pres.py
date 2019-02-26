#!/usr/bin/python

from datetime import date

#    if x is None     if id(x) == id(None)
#    if x == "NONE"

def mkdate(raw_date):
    if raw_date == "NONE":
        d = None
    else:
        raw_year, raw_month, raw_day = raw_date.split('-')
        d = date(int(raw_year),int(raw_month),int(raw_day))
    return d


def get_info(index):
    pres_data = {}
    with open("../DATA/presidents.txt") as pres_in:
        for line in pres_in:
            fields = line.rstrip().split(":")
            if int(fields[0]) == index:
                pres_data["lastname"] = fields[1]
                pres_data["firstname"] = fields[2]

                pres_data["birthdate"] = mkdate(fields[3])
                pres_data["deathdate"] = mkdate(fields[4])

                pres_data["birthplace"] = fields[5]
                pres_data["birthstate"] = fields[6]

                pres_data["termstart"] = mkdate(fields[7])
                pres_data["termend"] = mkdate(fields[8])

                pres_data["party"] = fields[9]

                break

    return pres_data

def get_all_data():
    """
    Make a list of dictionaries, one for each president.
    Thus, LIST[0] will be George Washington, and LIST[0]['last_name']
    will be last name, etc.

    :return: List of dictionaries
    """
    all_data = []
    for i in range(1,46):
        all_data.append(get_info(i))
    return all_data

