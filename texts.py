import csv
import json
import pandas as pd

with open('j000to100.json') as f:
    texts = json.load(f)
f.close
print(texts[0])
