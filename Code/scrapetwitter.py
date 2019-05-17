#Import the necessary methods from tweepy library

import tweepy
import re
import sys
import extract_feature_from_text
import sentiment_score_generater
from nltk.tokenize import WordPunctTokenizer
from bs4 import BeautifulSoup
import ocr


#Variables that contains the user credentials to access Twitter API 
access_token = "632679800-sjm8TRKEnW8veYiYvyJ7YB0sy9mrs85o3nxx22P2"
access_token_secret = "vxfOVBxfqRUvOxvSAlx8OQHmPBHVzETtwX9OzgpP7c4XP"
consumer_key = "MdrM4tJ6uXcNsjtd1nGbEuJXB"
consumer_secret = "vP0y8f5qv7zD59g1pq0bUhFdmCitrzsHHKCWjlxWJ7ktt9dYTS"

tok = WordPunctTokenizer()
pat1 = r'@[A-Za-z0-9]+'
pat2 = r'https?://[A-Za-z0-9./]+'
combined_pat = r'|'.join((pat1, pat2))
def tweet_cleaner(text):
    soup = BeautifulSoup(text, 'lxml')
    souped = soup.get_text()
    stripped = re.sub(combined_pat, '', souped)
    try:
        clean = stripped.decode("utf-8-sig").replace(u"\ufffd", "?")
    except:
        clean = stripped
    letters_only = re.sub("[^a-zA-Z0-9]", " ", clean)
    lower_case = letters_only.lower()
    words = tok.tokenize(lower_case)
    return (" ".join(words)).strip()


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)


def get_tweets(tweet_search):
    tweetsList = []
    for tweet in tweepy.Cursor(api.search,q=tweet_search,count=100,
                           lang="en",
                           since="2019-03-11").items():
        clean = tweet_cleaner(tweet.text.encode('utf-8'))
        tweetsList.append(clean)
    #print(tweetsList)
    tweet_sentence = ' '.join(tweetsList)
    print("\n--------spacy-----------------------\n")
    spacy_summarize_text=extract_feature_from_text.spacy_summarize(tweet_sentence)
    spacy_output_path = "../Data/output/spacy_twitter_summarized.txt"
    ocr.write_to_file(spacy_output_path,spacy_summarize_text)
    print("Extracted summary found in {}".format(spacy_output_path))
    print("\n======Sentiment Score=========\n")
    sentiment_score_generater.sentiment_score(spacy_summarize_text)



