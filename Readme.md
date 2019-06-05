[![Build Status](https://travis-ci.org/VidwathRHebse/SentenceSummarization.svg?branch=master)](https://travis-ci.org/VidwathRHebse/SentenceSummarization)

[![codecov](https://codecov.io/gh/VidwathRHebse/SentenceSummarization/branch/master/graph/badge.svg)](https://codecov.io/gh/VidwathRHebse/SentenceSummarization)

# Text Summarization and Sentiment Recognition:

## Steps to follow:

1. Install all the required libraries as InstallationRequirements.txt:
    pip install -r InstallationRequirements.txt

2. Run from terminal :

   a. cd SentecnceSummarization/Code

   b. python get_urls_from_google.py
   	   
   	    Enter the search query : <b> MG Hector Review</b>

   	    Result: 

   		--------spacy-----------------------

		Extracted summary found in ../Data/output/MG Hector Review/spacy_summarized.txt

		======Sentiment Score=========

		compound: 0.5994,neg: 0.0,neu: 0.965,pos: 0.035,

		--------Genism-----------------------

		Extracted summary found in ../Data/output/MG Hector Review/genism_summarized.txt

		======Sentiment Score from Genism=========

		compound: 0.9995,neg: 0.012,neu: 0.906,pos: 0.082




## Result:

	1. Text Summarization result of both Genism and Spacy will be saved in the folder creted by the search name
	2. Sentiment Score will be displayed.

## Future Scope:

1. Text Summarization can be delt with TFIDF : https://hackernoon.com/finding-the-most-important-sentences-using-nlp-tf-idf-3065028897a3
2. Text summarization using word2vec : https://hackernoon.com/finding-the-most-important-sentences-using-nlp-tf-idf-3065028897a3
3. Text Ranking along with GloVE : https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/ 
4. Use advance deep learning methods to get sentiment classification.
