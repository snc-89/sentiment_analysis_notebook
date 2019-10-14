#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sentiment as se
import nlp as n
import csv

from multiprocessing import Pool as ThreadPool

num_threads = 4


comments =  ['fuck your gay shit nigguh lmao you fucken gay prick']

# change to en_core_web_lg later on
n.nlp = n.load_spacy_db("en_core_web_sm")
se.read_sentiwords_file()


def start_threads(urld, num_threads):
    pool = ThreadPool(num_threads)
    pool.map(se.parse_comment, comments)
    pool.close()

if __name__ == '__main__':
    start_threads(comments, num_threads)
