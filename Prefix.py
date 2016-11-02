import requests
import json

url = "http://challenge.code2040.org/api/prefix"
API_TOKEN = 'cc58efad8d51fde5172b3d5e5ec94cfb'
data = {'token': API_TOKEN}

r = requests.post(url, data).json()

prefix = r["prefix"]
arrayStr = r["array"]

def find_all_with_prefix(prefix, arrayStr) :
    building_array = []
    prefixLen = len(prefix)
    for i in range(0, len(arrayStr)):
        if arrayStr[i].startswith(prefix) == False:
            building_array.append(arrayStr[i])
    return building_array

prefix_array = find_all_with_prefix(prefix, arrayStr)

returnData = {}
returnData['token'] = API_TOKEN
returnData['array'] = prefix_array

r = requests.post("http://challenge.code2040.org/api/prefix/validate",
json = returnData)

print(r.text)
print(prefix)
print(arrayStr)
print(prefix_array)
