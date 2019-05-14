#!/bin/sh
cd Code/Test
python test_for_features.py -v — with-coverage
python test_for_scrapetwitter.py -v — with-coverage
python test_for_spacy.py -v — with-coverage
python test_for_tesseract.py -v — with-coverage
python test_for_webscrapping.py -v — with-coverage