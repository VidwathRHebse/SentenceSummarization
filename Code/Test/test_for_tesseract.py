import unittest 
import sys
sys.path.insert(0, '../')
import ocr


class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test_for_image_to_txt(self):
    	text = ocr.image_to_txt('../../Data/input/test1.png')
    	# print(text)
    	original_text = 'PHOTOSHOP'
    	self.assertEqual(text,original_text) 
  
    def test_for_pdf_to_txt(self):
    	text = ocr.pdf_to_text('../../Data/input/test2.pdf')
    	# print(text)
    	original_text = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPhotoshop \n\n\n'
    	self.assertEqual(text,original_text) 
    	
if __name__ == '__main__': 
    unittest.main() 