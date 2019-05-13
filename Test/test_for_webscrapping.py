import unittest 
import sys
sys.path.insert(0, '/home/vidwath/Documents/SentecnceSummarization/Code/')
import webscrapping_new

class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test_for_clean_txt(self):
    	url = 'https://www.cartrade.com/bmw-cars/m3/reviews/m3-expert-reviews'
    	recieved_url = webscrapping_new.get_review_url(url)
    	#print(text)
    	actual_url = 'https://www.cartrade.com/bmw-cars/m3/reviews/m3-expert-reviews/206977.html'
    	self.assertEqual(actual_url,recieved_url) 
      	
if __name__ == '__main__': 
    unittest.main() 