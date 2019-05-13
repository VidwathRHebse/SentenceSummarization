import requests
from bs4 import BeautifulSoup
#import sys
#sys.path.insert(0, '/home/vidwath/Documents/SentecnceSummarization/Code/')
import extract_feature_from_text
import sentiment_score_generater
import re

def get_review_url(url):
    base_url = "https://www.cartrade.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    for data in soup.find_all('div', class_='rtitle'):
        for a in data.find_all('a'):
            url = base_url + a.get('href')
            break;
        break;
    print(url)
    return(url)

def get_summarization_and_sentiment_score(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    text =soup.find_all('p')
    str_cells = str(text)
    cleantext = BeautifulSoup(str_cells, "lxml").get_text()
    #print(cleantext)
    print("\n--------spacy-----------------------\n")
    spacy_summarize_text=extract_feature_from_text.spacy_summarize(cleantext)
    print(spacy_summarize_text)
    print("\n======Sentiment Score=========\n")
    sentiment_score_generater.sentiment_score(spacy_summarize_text)
    