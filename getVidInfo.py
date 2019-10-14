#!/usr/bin/python

import httplib2
import os
import sys
import csv
from googleapiclient.discovery import build
from apiclient.errors import HttpError
import json
import test

with open('vidIDs.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
f.close()
vids = your_list[0]

key = []
key.append('AIzaSyDyjx0PxmzDQsuob6TSpGrEufCAjePK5Fg')
key.append('AIzaSyBZNh5QZPbdOEPeE-sNZaP8F71Op-NDW-4')

youtube = test.builder('AIzaSyBZNh5QZPbdOEPeE-sNZaP8F71Op-NDW-4')

results = []
for i in range(len(vids)):
    results.append(youtube.videos().list(
        part='snippet',
        id=vids[i],
        fields='items(snippet(publishedAt))'
        ).execute())

json = json.dumps(results)
print(json)

with open('dates.json', 'w') as f:
    json.dump(results, f)
f.close()
