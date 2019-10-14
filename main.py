import json

with open('cleanDictArray.json') as f:
    vidDictArr = json.load(f)
f.close

with open('cleanDict1.json') as f:
    vidDict = json.load(f)
f.close

print(vidDictArr[0])
print(vidDict['JRE MMA Show #74 with Brendan Schaub'])
