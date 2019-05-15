#!/bin/sh
cd Code/Test
# coverage run -a test_for_features.py 
coverage run  test_for_scrapetwitter.py
coverage run  test_for_spacy.py
coverage run  test_for_tesseract.py 
coverage run  test_for_webscrapping.py 
