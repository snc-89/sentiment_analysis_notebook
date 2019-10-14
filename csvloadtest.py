import wikipedia
import csv
import re
import pandas as pd

with open('classeslist.csv', encoding='utf-8') as f:
    r = csv.reader(f)
    classes = list(r)
    classes = classes[0]
f.close()

for i in range(len(classes)):
    classes[i] = int(classes[i])

print(len(classes))