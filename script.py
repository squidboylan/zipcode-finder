from __future__ import print_function
import json
import sys
import zipcode

args = sys.argv

if "--list" in args:
    simple_output = True
    args.remove("--list")

else:
    simple_output = False

if len(args) <= 1:
    print("Please pass in the starting zipcode as arg 1 and the number of miles around the zipcode you wish to search as arg 2")
    print("example: python script.py [--list] <zip_code> <miles>")
    sys.exit(1)

start = zipcode.isequal(args[1])

zipcodes = zipcode.isinradius((start.lat, start.lon), args[2])

zipcode_list = []

for i in zipcodes:
    i_dict = i.to_dict()
    if i_dict['decommisioned'] == "FALSE":
        if simple_output:
            zipcode_list.append(i_dict['zip'])
        else:
            zipcode_list.append(i_dict)

print(json.dumps(zipcode_list))
