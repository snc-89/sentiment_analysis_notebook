#!/usr/bin/python

import httplib2
import os
import sys
import csv
from googleapiclient.discovery import build
from apiclient.errors import HttpError
import json
import test

with open('vidIDs2.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
f.close()
vids = your_list[0]

keys = []
keys.append('AIzaSyDyjx0PxmzDQsuob6TSpGrEufCAjePK5Fg')
keys.append('AIzaSyBZNh5QZPbdOEPeE-sNZaP8F71Op-NDW-4')
keys.append('AIzaSyCzH8b31cZcPSXibFFvqU4LwCQ-VjB9QFw')
keys.append('AIzaSyDfNrqG1h_ZvLZcO8yhTx0_guTpJxYHMe8')
keys.append('AIzaSyBqAqyexh0rgx9FL4AfQCWbHYCEYqv07ak')
keys.append('AIzaSyCGcbhNXnTtmPqj4fdTtkyYlKt_26mek0c')
keys.append('AIzaSyAuOOPQcmEMB1wSDX_nTwsGYOXh612kFKg')
keys.append('AIzaSyBsnDqKuSSJWlJW_yAZ1FV_E7LVPkj3Wkg')
keys.append('AIzaSyD_i4UHyOKUyzk13D4T9qR0YMmDHPz4QiY')
keys.append('AIzaSyDTjF-8riSCcjGA8L-QuGyofkftL5cQx3A')
keys.append('AIzaSyDIm9Ubegd2mpqhNJlkuu3FW-Tbn5EWRi4')
keys.append('AIzaSyAa6Csr1Tv_-CRUf9rwCXvIJguqI3GA_f8')
keys.append('AIzaSyB5iW8KXCcnPdQYIQGojP1ya5Xm2A4zY9w')
keys.append('AIzaSyAQqztCZOehqT_OlUDpAL9a6kXjX1-ylY4')#6
keys.append('AIzaSyCt2NC61eHY4DPcO5TMqzbDp9CB1QZMNoA')#7
keys.append('AIzaSyBmkGrIlu_dcfES8YlzdeP-IRI9os9HLag')#8
keys.append('AIzaSyB3YhD5oeZw6iP2CiV5zCATCb2z11K6eRE')#9
keys.append('AIzaSyC-LUwzG9MdkM5_pgsUkpPOyJ2jEiLa6PE')#10
keys.append('AIzaSyCbkCbhQmxV-8FKwdvj7yvnNtyPLd-TBpw')#11
keys.append('AIzaSyCfsLSZACim-yuI_v4qSICEqWg7nFBYF00')#12




youtube = test.builder(keys[-6])
def getComments(id):
    results = []
    i = 0
    next = None
    while True:
        results.append(youtube.commentThreads().list(
                part='snippet,replies',
                videoId=id,
                pageToken=next,
                maxResults=100,
                textFormat='plainText',
                fields='nextPageToken,items(replies(comments(snippet(textDisplay))),snippet(topLevelComment(snippet(textDisplay))))'
        ).execute())
        
        if 'nextPageToken' not in results[i]:
            break
        next = results[i]['nextPageToken']
        i = i + 1
    print("quota used:",(i*4))
    return results

allResults = []
with open('j1300-1394.json') as f:
    allResults = json.load(f)
f.close

print('scraping begins')
for i in range(1375,1394):
    allResults.append(getComments(vids[i]))
    print(str(i) + " complete")
    
with open('j1300-1394.json', 'w') as f:
    json.dump(allResults, f)
f.close
