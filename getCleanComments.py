import csv
import json

with open('unprocessedComments.json') as f:
    comments = json.load(f)
f.close

def listOfComments(arr):
    allComments = []
    for page in arr:
        for comments in page['items']:
            allComments.append(comments['snippet']['topLevelComment']['snippet']['textDisplay'].replace("\n", " ").replace("\r"," ").replace("\r\n"," "))
            if 'replies' in comments:
                for replies in comments['replies']['comments']:
                    allComments.append(replies['snippet']['textDisplay'].replace("\n", "").replace("\r"," ").replace("\r\n"," "))
    return allComments

count = 0
for texts in comments:
    foobar = listOfComments(texts)
    with open('cleanedComments.csv', 'a', newline='', encoding='utf-8') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(foobar)
    count = count+1
    print(count)

myfile.close()
