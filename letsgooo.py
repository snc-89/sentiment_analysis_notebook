#!/usr/bin/python

import httplib2
import os
import sys
import csv
from googleapiclient.discovery import build
from apiclient.errors import HttpError
import json
import test
import requests

with open("vidinfo.txt","r") as f:
    lst=f.read()
f.close()

thing = lst.split('}]},')
for i in range(len(thing)-1):
    thing[i] = thing[i] + '}]}'
thing[0] = thing[0][1:]


S = requests.Session()

url = "https://en.wikipedia.org/w/api.php"

params = {
    "action": "query",
    "prop": "links",
    "titles": "List of male mixed martial artists",
    "format": "json",
    "plcontinue": None,
    "pllimit":500
}
data = []
for i in range(4):
    R = S.get(url=url, params=params)
    data.append(R.json())
    params['plcontinue'] = data[i]['continue']['plcontinue']
    if i == 2:
        params['pllimit'] = 443

arr = []
for k in range(len(data)):
    thing = data[k]['query']['pages']['1326282']['links']
    for i in range(len(thing)):
        arr.append(thing[i]['title'])

with open('fighternames.csv', 'w', newline='',encoding='utf-8') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(arr)
myfile.close()


def getNames(params):
    data = []
    i = 0
    while True:
        R = S.get(url=url, params=params)
        data.append(R.json())
        if 'batchcomplete' in data[i]:
            break
        params['plcontinue'] = data[i]['continue']['plcontinue']
        i=i+1

    
    arr = []
    for k in range(len(data)):
        thing = data[k]['query']['pages']['1326282']['links']
        for i in range(len(thing)):
            arr.append(thing[i]['title'])
    return arr
        

params = {
    "action": "query",
    "prop": "links",
    "titles": "List of male mixed martial artists",
    "format": "json",
    "plcontinue": None,
    "pllimit":500
}
foo = getNames(params)


print(foo)
