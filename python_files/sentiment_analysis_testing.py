import json
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score

with open('vader_texts_and_scores.json') as f:
    vader_sentiments = json.load(f)
f.close
with open('foobar.json', 'r') as f:
    our_sentiments = json.load(f)
f.close

#turn sentiment scores into negative (-1), neutral(0), positive(1) categories
def categorise_scores(dictionary):
    for i,text in enumerate(dictionary['vader']):
        if text['sentiment'] > 0:
            dictionary['vader'][i]['sentiment'] = 1
            continue
        if text['sentiment'] < 0:
            dictionary['vader'][i]['sentiment'] = -1
            continue
        dictionary['vader'][i]['sentiment'] = 0

categorise_scores(vader_sentiments)
categorise_scores(our_sentiments)

#extracting texts and scores from dictionaries as lists to turn into dataframe
vader_texts, vader_scores, our_texts, our_scores, our_magnitude = ([] for i in range(5))
for vader,ours in zip(vader_sentiments['vader'],our_sentiments['vader']):
    vader_texts.append(vader['text'])
    vader_scores.append(vader['sentiment'])
    our_texts.append(vader['text'])
    our_scores.append(ours['sentiment'])
    our_magnitude.append(ours['magnitude'])

#turn to dataframes and sort them by text alphabetically because they're not in the same order initially
vaders = pd.DataFrame({'texts': vader_texts, 'y_true': vader_scores})
ours = pd.DataFrame({'texts': our_texts,'pred': our_scores,'magnitude': our_magnitude})
vaders.sort_values(by=['texts'])
ours.sort_values(by=['texts'])

#join the dataframes together and filter out 0 values
df = pd.concat([ours,vaders], axis=1)
sans_0 = df[(df.pred != 0) & (df.y_true != 0)]
y_true = sans_0.y_true
prediction = sans_0.pred
print("accuracy score:  ",accuracy_score(y_true, prediction))