import requests
import json

r = requests.post("http://challenge.code2040.org/api/reverse",
data = {'token': 'cc58efad8d51fde5172b3d5e5ec94cfb'})
r = r.text[::-1]

r = requests.post("http://challenge.code2040.org/api/reverse/validate",
data = {'token': 'cc58efad8d51fde5172b3d5e5ec94cfb', 'string': r})
