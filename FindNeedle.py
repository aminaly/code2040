import requests
import json

url = "http://challenge.code2040.org/api/haystack"
data = {'token': 'cc58efad8d51fde5172b3d5e5ec94cfb'}

r = requests.post("http://challenge.code2040.org/api/haystack", data).json()

needleVal = r["needle"]
haystack = r["haystack"]

def find_needle(tofind, list) :
    for val in range(len(list)):
        if list[val] == tofind:
            return val
    return -1

indexVal = find_needle(needleVal, haystack)

# There is an easier way to do this (below) using index.
indexVal2 = haystack.index(needleVal)

returnData = {'token': 'cc58efad8d51fde5172b3d5e5ec94cfb', 'needle': indexVal}
r = requests.post("http://challenge.code2040.org/api/haystack/validate",
returnData)

print(r)
