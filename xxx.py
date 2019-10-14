import json
import csv


with open('vidIDs.csv') as f:
    reader = csv.reader(f)
    your_list = list(reader)
f.close()
vids = your_list[0]

del vids[1298]
del vids[1205]
del vids[1055]
del vids[1034]
del vids[671]

with open('vidIDs2.csv', 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     wr.writerow(vids)
myfile.close()
