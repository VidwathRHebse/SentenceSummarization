import unittest 
import sys
sys.path.insert(0, '../')
import extract_feature_from_text
import ocr


class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test_for_spacy(self):
        text = ocr.pdf_to_text('/home/vidwath/Documents/SentecnceSummarization/Data/input/sample3.pdf')
        summary = extract_feature_from_text.spacy_summarize(text)
    	# print(text)
        expected_summary_len = 923
        self.assertEqual(len(summary),expected_summary_len) 
  
    def test_for_genism(self):
        text = ocr.pdf_to_text('/home/vidwath/Documents/SentecnceSummarization/Data/input/sample3.pdf')
    	# print(text)
        summary = extract_feature_from_text.genism_summarize(text)
        expected_summary_len = 1034
        self.assertEqual(len(summary),expected_summary_len) 
    	
if __name__ == '__main__': 
    unittest.main() 