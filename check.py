import json

with open('j3.json') as f:
    datastore = json.load(f)
f.close

print(datastore[0])
