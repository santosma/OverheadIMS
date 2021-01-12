import pytesseract
import os
from decouple import config
try:
    from PIL import Image
except ImportError:
    import Image




def ocr_processing(filename):
    pytesseract.pytesseract.tesseract_cmd = config('OCR_PATH')
    text = pytesseract.image_to_string(Image.open(filename))
    return(text)
