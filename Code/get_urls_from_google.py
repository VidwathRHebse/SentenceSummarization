import os
from googlesearch import search
from selenium import webdriver
import Screenshot_taker
import ocr
import sentiment_score_generater
import extract_feature_from_text

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=options)

query = input('Enter the search query : ')

dir_name = '../Data/output/' + query

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print("Directory ", dir_name, " Created ")
else:
    print("Directory ", dir_name, " already exists")

ocr_text = []
for url in search(query, tld='com', stop=10):
    print(url)
    if 'youtube' not in str(url):
        output_path = '../Data/output/' + query + '/'
        output_path = output_path + url.split("//")[1].split("/")[0] + ".png"
        print(output_path)
        output_path = Screenshot_taker.save_fullpage_screenshot(
            driver, url, output_path)
        ocr_text.append(ocr.image_to_txt(output_path))

ocr_sentence = ' '.join(ocr_text)
print("\n--------spacy-----------------------\n")
spacy_summarize_text = extract_feature_from_text.spacy_summarize(ocr_sentence)
spacy_output_path = dir_name + "/spacy_summarized.txt"
ocr.write_to_file(spacy_output_path, spacy_summarize_text)
print("Extracted summary found in {}".format(spacy_output_path))
print("\n======Sentiment Score=========\n")
sentiment_score_generater.sentiment_score(spacy_summarize_text)
genism_summarize_text = extract_feature_from_text.genism_summarize(
    ocr_sentence)
genism_output_path = dir_name + "/genism_summarized.txt"
ocr.write_to_file(genism_output_path, genism_summarize_text)
print("\n--------Genism-----------------------\n")
print("Extracted summary found in {}".format(genism_output_path))
print("\n======Sentiment Score from Genism=========\n")
sentiment_score_generater.sentiment_score(genism_summarize_text)

driver.quit()
