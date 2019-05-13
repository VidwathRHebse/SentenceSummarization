import cv2
import pytesseract
from PIL import Image
from tika import parser
import os

def image_to_txt(path):
    # Load the required image
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    preprocess = False
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    # Store grayscale image as a temporary file to apply OCR
    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)

        # Load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    return(text)

def pdf_to_text(path):
    # Parse data from file
    file_data = parser.from_file(path)
    # Get files text content
    text = file_data['content']
    return(text)

def write_to_file(out_path,text):
    text_file = open(out_path, "w")
    text_file.write(text)
    text_file.close()  

