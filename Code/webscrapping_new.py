import requests
from bs4 import BeautifulSoup
import extract_feature_from_text
import sentiment_score_generater
import re
import ocr

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
    spacy_output_path = "../Data/output/spacy_web_summarized.txt"
    ocr.write_to_file(spacy_output_path,spacy_summarize_text)
    print("Extracted summary found in {}".format(spacy_output_path))
    print("\n======Sentiment Score=========\n")
    sentiment_score_generater.sentiment_score(spacy_summarize_text)
    print("\n--------Google Genism-----------------------\n")
    genism_summarize_text=extract_feature_from_text.genism_summarize(cleantext)
    genism_output_path = "../Data/output/genism_web_summarized.txt"
    ocr.write_to_file(genism_output_path,genism_summarize_text)
    print("\n======Sentiment Score from Genism=========\n")
    sentiment_score_generater.sentiment_score(genism_summarize_text)
    