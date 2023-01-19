import pytesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\tessaract\tesseract-ocr-w64-setup-5.3.0.20221222.exe "


def convert():
    img = Image.open('image.jpg')
    text = pytesseract.image_to_string(img)
    print(text)
    
convert()