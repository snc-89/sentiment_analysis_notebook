import csv
import json

with open('vidIDs.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
f.close()
vids = your_list[0]

with open('j000to100.json') as f:
    text1 = json.load(f)
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

for texts in text1:
    foobar = listOfComments(texts)
    with open('comms.csv', 'a', newline='', encoding='utf-8') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(foobar)

myfile.close()
