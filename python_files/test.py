#!/usr/bin/python

import httplib2
import os
import sys
import csv
from googleapiclient.discovery import build
from apiclient.errors import HttpError
import json

key='AIzaSyCuyoI8j5yOFRsnnumz9GgqYNmT-1gLayk'

def builder(devkey):
    return build(
    'youtube','v3',
    developerKey=devkey
    )

youtube = builder(key)

def playlistItems(ID,num):
    results = []
    nextToken = None
    max = 50
    for i in range(num):
        results.append(youtube.playlistItems().list(
            part='contentDetails',
            pageToken = nextToken,
            playlistId=ID,
            maxResults=max
        ).execute())
        if i==(num-1):
            nextToken = None
        else:
            nextToken = results[i]['nextPageToken']    
    return results

def getIDs(arr):
    IDs = []
    for i in arr:
        for k in i['items']:
            IDs.append(k['contentDetails']['videoId'])
    return IDs







