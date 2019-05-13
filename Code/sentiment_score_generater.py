#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:54:14 2019

@author: vidwath
"""

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
from nltk.sentiment.vader import SentimentIntensityAnalyzer


sid = SentimentIntensityAnalyzer()

def sentiment_score(contents):
    scores = sid.polarity_scores(contents)
    for key in sorted(scores):
        print('{0}: {1},'.format(key, scores[key]), end = '')
