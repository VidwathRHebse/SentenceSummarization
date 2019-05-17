#import sys
#sys.path.insert(0, '/home/vidwath/Documents/SentecnceSummarization/Code/')
import webscrapping_new
import scrapetwitter
import ocr
import os
import extract_feature_from_text
import sentiment_score_generater


make = ['Audi','BMW','Volvo']
model_audi = ['A3','A4','A6','Q3','Q5','Q7']
model_bmw =['M3','M5','M6']
model_volvo = ['XC40','XC60','XC90']

def choose_scraping_site():
    print("\n---1. Twitter----")
    print("\n---2. Expert Review----")
    print("\n---3. PDF or PNG from Location----")
    index = input('Enter the option from above : ')
    if index == '1':
        print("\nEnter the hash tag with model name ex: {}".format("#XC90"))
        model = input('Enter the model with # : ')
        scrapetwitter.get_tweets(model)
    elif index == '2' :
        display_and_choose_make()
    elif index == '3' :
        pdf_image_processor()
    else :
        print("Please enter the correct choice by number ex: 1")
        choose_scraping_site()


def pdf_image_processor():
    print("\n--------------------")
    file = input('Enter the location of file: ')
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension.lower()
    list_img = [".png",".jpg",".jpeg"]
    if any(file_extension in s for s in list_img) : 
        text = ocr.image_to_txt(file)
    else :
        text = ocr.pdf_to_text(file)
    print("\n--------Spacy-----------------------\n")
    spacy_summarize_text=extract_feature_from_text.spacy_summarize(text)
    spacy_output_path = "../Data/output/spacy_summarized.txt"
    print(spacy_output_path)
    ocr.write_to_file(spacy_output_path,spacy_summarize_text)
    print("Extracted summary found in {}".format(spacy_output_path))
    #print(spacy_summarize_text)
    print("\n======Sentiment Score from Spacy=========\n")
    sentiment_score_generater.sentiment_score(spacy_summarize_text)
    print("\n--------Google Genism-----------------------\n")
    genism_summarize_text=extract_feature_from_text.genism_summarize(text)
    genism_output_path = "../Data/output/genism_summarized.txt"
    ocr.write_to_file(genism_output_path,genism_summarize_text)
    print("Extracted summary found in {}".format(genism_output_path))
    print("\n======Sentiment Score from Genism=========\n")
    sentiment_score_generater.sentiment_score(genism_summarize_text)



def display_and_choose_make():
    print(make)
    print('\n')
    make_selected = input('Select the make from above list: ')
    #print(make_selected)
    choose_model(make_selected)

def choose_model(make_selected):
    if make_selected.lower() == 'audi':
        print(model_audi)
        model_selected = input('Select the model from above list: ')
    elif make_selected.lower() == 'bmw':
        print(model_bmw)
        model_selected = input('Select the model from above list: ')
    elif make_selected.lower() == 'volvo':
        print(model_volvo)
        model_selected = input('Select the model from above list: ')
    print("Make and Model choosen are : {} {}".format(make_selected,model_selected))
    generate_url(make_selected,model_selected)


def generate_url(make_selected,model_selected):
    base_url = "https://www.cartrade.com/"
    final_url = base_url + make_selected.lower() + "-cars/" + model_selected.lower() + "/reviews/" +  model_selected.lower() + "-expert-reviews"
    print("\n========Review URL=======\n")
    print(final_url)
    url = webscrapping_new.get_review_url(final_url)
    webscrapping_new.get_summarization_and_sentiment_score(url)



try:
    if __name__ == "__main__":
        choose_scraping_site()
except Exception as e:
    print(e.args)
    print(e.__cause__)
