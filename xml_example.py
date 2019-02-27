#!/usr/bin/env python
# import xml.etree.ElementTree as ET
import lxml.etree as ET

doc = ET.parse('DATA/presidents.xml')

print(doc)

# pres_list = doc.getroot()
#
# print(pres_list)
# for pres in pres_list:
#     name = pres.find('name')
#     first_name = name.find('first').text
#     last_name = name.find('last').text
#     print(first_name, last_name)

for name in doc.findall('.//name'):
    first_name = name.findtext('first')
    last_name = name.findtext('last')
    print(f'{first_name:25.25s} {last_name}')

for i in range(10):
    print(i)
