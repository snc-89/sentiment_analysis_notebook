#!/usr/bin/python

import csv
import json
import requests
import wikipedia

def get_page_id(page_title):
    S = requests.Session()
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "action": "query",
        "format": "json",
        "titles": page_title,
        "prop": "info",
    }
    R = S.get(url=URL, params=PARAMS)
    data = R.json()
    return (list(data['query']['pages'].keys())[0])

def get_names(page_name):
    S = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    page_id = get_page_id(page_name)
    params = {
    "action": "query",
    "prop": "links",
    "titles": page_name,
    "format": "json",
    "plcontinue": None,
    "pllimit":500
    }

    data = []
    i = 0
    while True:
        R = S.get(url=url, params=params)
        data.append(R.json())
        if 'batchcomplete' in data[i]:
            break
        params['plcontinue'] = data[i]['continue']['plcontinue']
        i=i+1

    
    names = []
    for k in range(len(data)):
        links = data[k]['query']['pages'][page_id]['links']
        for i in range(len(links)):
            names.append(links[i]['title'])
    return names
        

scientists = get_names('List of United States stand-up comedians')

with open('americanComedians.csv', 'w', newline='',encoding='utf-8') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(scientists)
myfile.close()
