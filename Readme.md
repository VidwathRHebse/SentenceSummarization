[![Build Status](https://travis-ci.org/VidwathRHebse/SentenceSummarization.svg?branch=master)](https://travis-ci.org/VidwathRHebse/SentenceSummarization)

[![codecov](https://codecov.io/gh/VidwathRHebse/SentenceSummarization/branch/master/graph/badge.svg)](https://codecov.io/gh/VidwathRHebse/SentenceSummarization)

# Text Summarization and Sentiment Recognition:

## Steps to follow:

1. Install all the required libraries as present InstallationRequirements.txt
2. Run from terminal :

   a. cd SentecnceSummarization/Code

   b. python app.py
   	   
   	    i. Select from the below options:   	   		
   	   		---1. Twitter----
			---2. Expert Review----
			---3. PDF or PNG from Location----
			Enter the option from above : 

		ii. If '1' is choosen it will query the data from twitter:
			a. Enter the model with # : '#XC90'

		iii. If '2' is choosen it will scrape the data from webpage:
			a. It will display the vehicle company list : Enter a company name as below
			Select the make from above list: 'Audi'
			b. Then it will display all the models of the company : choose a model to get summary
			Select the model from above list: 'A3'

		iv. If '3' is choosen it will ask for a png of pdf file from local : Enter the absolute path for the file
			Enter the location of file: /home/vidwath/Documents/SentecnceSummarization/Data/input/sample3.pdf



## Result:

	1. Text Summarization result will be saved to file in the output folder
	2. Sentiment Score will be displayed.

## Future Scope:

1. Text Summarization can be delt with TFIDF : https://hackernoon.com/finding-the-most-important-sentences-using-nlp-tf-idf-3065028897a3
2. Text summarization using word2vec : https://hackernoon.com/finding-the-most-important-sentences-using-nlp-tf-idf-3065028897a3
3. Text Ranking along with GloVE : https://www.analyticsvidhya.com/blog/2018/11/introduction-text-summarization-textrank-python/ 
4. Use advance deep learning methods to get sentiment classification.
5. Add more vehicle listing in the expert review section.
