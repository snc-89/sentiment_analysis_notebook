#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nlp as n
import scrape as sc
import sentiment as se


def compile_entity_data(entities):
    exist = False
    already_listed = list()
    data = list()

    for entity in entities:
        if entity.text in already_listed or len(entity.text) <= 2 \
                                         or ("\\") in entity.text:
            break

        already_listed.append(entity.text)

        entity_data = {
            'name': entity.text,
            'type': entity.label_,
        }

        data.append(entity_data)
        exist = True

    return data, exist


def compile_sentence_data(sentences):
    exist = False
    data = list()

    for tokens in sentences:
        magnitude, sentiment = se.calculate_magnitude_sentiment(tokens)
        sentence = n.get_text_str_from_tokens(tokens)

        # Working around Python's weird float rounding quirk
        magnitude = round(magnitude, 2)
        sentiment = round(sentiment, 2)

        if magnitude == -0:
            magnitude = 0

        if sentiment == -0:
            sentiment = 0

        if len(sentence) > 5:
            sentence_data = {
                'sentiment': {
                    'magnitude': magnitude,
                    'score': sentiment
                },
                'text': {
                    'beginOffset': tokens[0].offset,
                    'content': sentence
                },
            }

            data.append(sentence_data)
            exist = True

    return data, exist


def compile_general_data(comment):
    features = []

    tokens, sentences, entities = n.analyse_text(comment)
    magnitude_text, sentiment_text = se.calculate_magnitude_sentiment(tokens)

    # Working around Python's weird float rounding quirk
    magnitude_text = round(magnitude_text, 2)
    sentiment_text = round(sentiment_text, 2)

    if magnitude_text == -0:
        magnitude_text = 0

    if sentiment_text == -0:
        sentiment_text = 0

    sentence_data, sentence_feature = compile_sentence_data(sentences)
    entity_data, entity_feature = compile_entity_data(entities)

    if sentence_feature:
        features.append("sentences")

    if entity_feature:
        features.append("entities")

    data = {
        'text': comment,
        'sentences': sentence_data,
        'entities': entity_data,
        'documentSentiment': {
            'magnitude': magnitude_text,
            'score': sentiment_text,
        },
    }

    return data, features
