#!/usr/bin/python

# Usage example:
# python comments.py --videoid='<video_id>' --text='<text>'

import httplib2
import os
import sys

from googleapiclient.discovery import build
from apiclient.discovery import build_from_document
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
import json



CLIENT_SECRETS_FILE = "client_secrets.json"


YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# This variable defines a message to display if the CLIENT_SECRETS_FILE is
# missing.

# Authorize the request and store authorization credentials.
def get_authenticated_service():
  return build('youtube','v3',developerKey='AIzaSyCuyoI8j5yOFRsnnumz9GgqYNmT-1gLayk')


# Call the API's commentThreads.list method to list the existing comment threads.
def get_comment_threads(youtube, video_id):
  results = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText"
  ).execute()

  for item in results["items"]:
    comment = item["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print ("Comment by %s: %s" % (author, text))

  with open('out.json','w') as fp:
    json.dump(results,fp)
	
  fp.close()
  return results["items"]


# Call the API's comments.list method to list the existing comment replies.
def get_comments(youtube, parent_id):
  results = youtube.comments().list(
    part="snippet",
    parentId=parent_id,
    textFormat="plainText"
  ).execute()

  for item in results["items"]:
    author = item["snippet"]["authorDisplayName"]
    text = item["snippet"]["textDisplay"]
    print ("Comment by %s: %s" % (author, text))

  return results["items"]


if __name__ == "__main__":



  youtube = get_authenticated_service()
  # All the available methods are used in sequence just for the sake of an example.
  try:
    video_comment_threads = get_comment_threads(youtube, 'bgr4jP4wVyY')
    parent_id = video_comment_threads[0]["id"]
    video_comments = get_comments(youtube, parent_id)
  except HttpError as e:
    print ("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
  else:
    print ("Inserted, listed, updated, moderated, marked and deleted comments.")
