import unittest 
import sys
sys.path.insert(0, '../')
import extract_feature_from_text
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
stopwords = list(STOP_WORDS)
nlp = spacy.load('en')
document = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""
docx = nlp(document)

class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test_for_word_frequencies(self):
        word_freq = extract_feature_from_text.word_frequencies(docx)
        expected_word_freq_len = 73
        self.assertEqual(len(word_freq),expected_word_freq_len) 
    
    def test_for_sentence_generation(self):
        word_freq = extract_feature_from_text.word_frequencies(docx)
        sent_scores= extract_feature_from_text.sentence_scores(docx,word_freq)
        expected_number_of_sentences = 7
        recieved_number_of_sentences = len(str(sent_scores).split(":"))
        self.assertEqual(expected_number_of_sentences,recieved_number_of_sentences) 
    
    def test_for_summarise_sentence_heapq(self):
        word_freq = extract_feature_from_text.word_frequencies(docx)
        sent_scores= extract_feature_from_text.sentence_scores(docx,word_freq)
        summary = extract_feature_from_text.summarize_sentence_heapq(sent_scores)
        expected_length = 843
        recieved_length = len(summary)
        self.assertEqual(expected_length,recieved_length)

    def test_for_genism(self):
        summary = extract_feature_from_text.genism_summarize(document)
        expected_length = 195
        recieved_length = len(summary)
        self.assertEqual(expected_length,recieved_length)  

  
        
if __name__ == '__main__': 
    unittest.main() 