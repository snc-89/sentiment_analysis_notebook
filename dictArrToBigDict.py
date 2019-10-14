import json
import csv

with open('cleanDictArray.json') as f:
    datastore = json.load(f)
f.close

singleDict = dict()
for i in range(len(datastore)):
    singleDict[datastore[i]['title']] = datastore[i]
    singleDict[datastore[i]['title']].pop('title', None)

print(singleDict)

with open('cleanDict1.json', 'w') as f:
    json.dump(singleDict, f)
f.close
