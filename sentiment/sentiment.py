#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import math
import json
import json_output as jo
from dataclasses import dataclass

@dataclass
class Sentiment:
    lemma: str
    pos: str
    score: float

sentiwords_fps = 'resources/SentiWords_1.0.txt'
sentiments = []


def read_sentiwords_file():
    with open(sentiwords_fps) as senti_f:
        r = csv.reader(senti_f, delimiter='\t')

        for row in r:
            sentiments.append(Sentiment(row[0].split('#')[0],
                                        row[0].split('#')[1],
                                        row[1]))


def find_sentiment(lemma):
    for sentiment in sentiments:

        if lemma == sentiment.lemma:
            return float(sentiment.score)

    return 0.0  # Return default value if not found in 'sentiments'.


def calculate_magnitude_sentiment(tokens):
    total_score = 0.0
    word_matches = 0
    total_abs = 0.0
    total_non_stopwords = 0

    for token in tokens:
        if not token.stopword:
            total_non_stopwords += 1

        if not token.sentiment == 0:
            total_score += token.sentiment
            total_abs += token.sentiment ** 2
            word_matches += 1

    if word_matches == 0:
        return 0.0, 0.0

    return math.sqrt(total_abs) * (word_matches / total_non_stopwords) * 100\
        if total_non_stopwords > 0 else 0,\
        total_score/word_matches


def parse_comment(comment):
    try:
        data, features = jo.compile_general_data(comment)
        print(data)
    except:  # noqa: E722
        pass
