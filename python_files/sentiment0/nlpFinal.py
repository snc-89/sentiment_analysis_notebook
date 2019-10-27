#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from dataclasses import dataclass
import multiprocessing
from multiprocessing import Pool as ThreadPool
import en_core_web_sm
import math
import json
import time

@dataclass
class Sentiment:
    lemma: str
    pos: str
    score: float

class Token:
    text = ''
    pos = ''
    lemma = ''
    sentiment = 0
    stopword = False

    def __init__(self, text, pos, lemma, sentiment, stopword):
        self.text = text
        self.pos = pos
        self.lemma = lemma
        self.sentiment = sentiment
        self.stopword = stopword


pos_comments = 1
sentiwords_fp = 'resources/SentiWords_1.0.txt'
sentiments = []
comments_fp = "1700comments.csv"
comments = []
all_comments = []
num_threads = multiprocessing.cpu_count()-1
nlp = en_core_web_sm.load()


def read_comments():
    with open(comments_fp, encoding="utf8") as comment_f:
        r = csv.reader(comment_f, delimiter=',')

        for row in r:
            comments = []

            for comment in row:
                comments.append(comment)

            all_comments.append(comments)


def start_threads(num_threads, comments):
    pool = ThreadPool(num_threads)
    pool.map(parse_comment, comments)
    pool.close()


def read_sentiwords_file():
    with open(sentiwords_fp) as senti_f:
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


def analyse_text(text):
    tokens = list()
    doc = nlp(text)

    for token in doc:
        if not token.is_stop:
            token_sentiment = find_sentiment(token.lemma_)
        else:
            token_sentiment = 0.0

        t = Token(token.text,
                token.pos_,
                token.lemma_,
                token_sentiment,
                token.is_stop)

        tokens.append(t)

    return tokens


def get_text_str_from_tokens(tokens):
    return (" ".join("".join(token.text) for token in tokens))


def parse_comment(comment):
    try:
        compile_general_data(comment)
    except:  # noqa: E722
        pass


def compile_general_data(comment):
    tokens = analyse_text(comment)
    magnitude_text, sentiment_text = calculate_magnitude_sentiment(tokens)

    # Working around Python's weird float rounding quirk
    magnitude_text = round(magnitude_text, 2)
    sentiment_text = round(sentiment_text, 2)

    if magnitude_text == -0:
        magnitude_text = 0

    if sentiment_text == -0:
        sentiment_text = 0

    data = {
        'text': comment,
        'video': pos_comments,
        'magnitude': magnitude_text,
        'sentiment': sentiment_text,
    }
    print(sentiment_text, magnitude_text)
    # print(json.dumps(data, indent=4, ensure_ascii=False),",",sep="")


def main():
    read_comments()
    read_sentiwords_file()

    global pos_comments

    for comments in all_comments:
        start_threads(num_threads, comments)
        pos_comments += 1
    
    time.sleep(10)


if __name__ == '__main__':
    main()