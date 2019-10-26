#!/usr/bin/python

import httplib2
import os
import sys
import csv
from googleapiclient.discovery import build
from apiclient.errors import HttpError
import json
import test
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

wiki = wiki_wiki.page('Python_(programming_language)')

with open('vidIDs.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
f.close()
vids = your_list[0]

youtube = test.builder()

results = dict()
for i in range(len(vids)):
    results["'"+str(i)+"'"] = youtube.videos().list(
        part='snippet,statistics',
        id=vids[i],
        fields='items(statistics,snippet(title))'
        ).execute()

print(results)

