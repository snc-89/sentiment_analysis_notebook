#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import spacy
import sentiment as se

nlp = 0


class Token:
    text = ''
    pos = ''
    lemma = ''
    sentence = 0
    paragraph = 0
    offset = 0
    length = 0
    sentiment = 0
    stopword = False

    def __init__(self, text, pos, lemma, sentence, paragraph, offset, length,
                 sentiment, stopword):
        self.text = text
        self.pos = pos
        self.lemma = lemma
        self.sentence = sentence
        self.paragraph = paragraph
        self.offset = offset
        self.length = length
        self.sentiment = sentiment
        self.stopword = stopword


def load_spacy_db(db):
    return spacy.load(db)


# tokenize_text tokenizes a given text
# iterating through each sentence and token.
def analyse_text(text):
    doc_s = nlp(text)
    offset = 0
    tokens = list()
    entities = list()

    paragraph_index = 0
    # paragraphs = list()
    sentence_index = 0
    sentences = list()

    # might use noun_chunks for modifiers
    # for item in doc_s.noun_chunks:
    #    print(item.text)

    for ent in doc_s.ents:
        entities.append(ent)

    for sentence in doc_s.sents:
        doc_t = nlp(str(sentence))
        sentence_tokens = list()

        for token in doc_t:
            token_length = len(token.text)

            if token.is_space and token.text.count('\n') > 1:
                paragraph_index += 1

            if not token.is_stop:
                token_sentiment = se.find_sentiment(token.lemma_)
            else:
                token_sentiment = 0.0

            t = Token(token.text,
                      token.pos_,
                      token.lemma_,
                      sentence_index,
                      paragraph_index,
                      offset,
                      token_length,
                      token_sentiment,
                      token.is_stop)

            offset += len(token.text)
            tokens.append(t)
            sentence_tokens.append(t)

        sentence_index += 1
        sentences.append(sentence_tokens)

    # Not necessary for now
    # bigrams, trigrams = get_ngrams(doc_s)

    return tokens, sentences, entities


def get_text_str_from_tokens(tokens):
    return (" ".join("".join(token.text) for token in tokens))