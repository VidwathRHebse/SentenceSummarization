import unittest 
import sys
sys.path.insert(0, '/home/vidwath/Documents/SentecnceSummarization/Code/')
import scrapetwitter

class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test_for_clean_txt(self):
    	uncleaned_text = 'The 2019 #Volvo #XC90 \xf0\x9f\x98\x8d \nCurrent Price - \xc2\xa354,000 \xf0\x9f\x92\xb8\nCurrent Mileage - 100 miles on the clock \xe2\x8f\xb0\n#Follow the link to\xe2\x80\xa6 https://t.co/guFOVxkoUi'
    	text = scrapetwitter.tweet_cleaner(uncleaned_text)
    	#print(text)
    	original_text = 'the 2019 volvo xc90 current price 54 000 current mileage 100 miles on the clock follow the link to'
    	self.assertEqual(text,original_text) 
      	
if __name__ == '__main__': 
    unittest.main() 