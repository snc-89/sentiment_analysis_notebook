import json
import csv

with open('info.json') as f:
    datastore = json.load(f)
f.close()

with open('dates.json') as f:
    dates = json.load(f)
f.close()

with open('vidIDs.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
f.close()
vids = your_list[0]

del datastore[1298]
del datastore[1205]
del datastore[1055]
del datastore[1034]
del datastore[671]
del dates[1298]
del dates[1205]
del dates[1055]
del dates[1034]
del dates[671]



nullIdx = []
for i in range (len(datastore)):
    if datastore[i]['items']==[]:
        nullIdx.append(i)

print(nullIdx)
arr = []
i = 0


for i in range(len(datastore)):
    temp = dict()
    temp['title'] = datastore[i]['items'][0]['snippet']['title']
    temp['viewCount'] = datastore[i]['items'][0]['statistics']['viewCount']
    temp['likeCount'] = datastore[i]['items'][0]['statistics']['likeCount']
    temp['dislikeCount'] = datastore[i]['items'][0]['statistics']['dislikeCount']
    temp['commentCount'] = datastore[i]['items'][0]['statistics']['commentCount']
    temp['date'] = dates[i]['items'][0]['snippet']['publishedAt']
    arr.append(temp)

print(len(arr))
with open('cleanDictArray2.json', 'w') as f:
    json.dump(arr, f)
f.close()
