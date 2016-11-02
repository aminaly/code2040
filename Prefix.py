import requests
import json

url = "http://challenge.code2040.org/api/prefix"
data = {'token': 'cc58efad8d51fde5172b3d5e5ec94cfb'}

r = requests.post(url, data).json()

prefix = r["prefix"]
arrayStr = r["array"]

def find_all_with_prefix(prefix, arrayStr) :
    building_array = []
    prefixLen = len(prefix)
    for val in range(len(arrayStr)):
        if len(arrayStr[val]) < prefixLen:
            continue
        if arrayStr[val][:prefixLen] == prefix:
            building_array.append(unicode(arrayStr[val]))
    return building_array

prefix_array = find_all_with_prefix(prefix, arrayStr)
prefix_array = json.dumps(prefix_array)


returnData = {'token': 'cc58efad8d51fde5172b3d5e5ec94cfb',
'array': prefix_array}

r = requests.post("http://challenge.code2040.org/api/prefix/validate",
returnData)

print(r)
