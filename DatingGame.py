import requests
import json
import datetime
import dateutil.parser

url_r = "http://challenge.code2040.org/api/dating"
url_s = url_r + '/validate'
API_TOKEN = 'cc58efad8d51fde5172b3d5e5ec94cfb'
data = {'token': API_TOKEN}

r = requests.post(url_r, json = data).json()

datestamp = r['datestamp'] # ISO 8601 datestamp
interval = r['interval'] #in seconds

timestamp = dateutil.parser.parse(datestamp)
new_time = timestamp + datetime.timedelta(0, interval)

new_time = new_time.isoformat()
new_time = new_time[:-6] + "Z"

returnData = {}
returnData['token'] = API_TOKEN
returnData['datestamp'] = new_time

print(datestamp)
print(interval)
print(new_time)

r = requests.post(url_s, json = returnData)

print(r.text)
