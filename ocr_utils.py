import pytesseract
from pdf2image import convert_from_path

def perform_ocr(pdf_path, page_number):
    images = convert_from_path(
        pdf_path,
        first_page=page_number + 1,
        last_page=page_number + 1
    )

    if not images:
        #Page could not be converted to image
        return ""

    text = pytesseract.image_to_string(images[0])
    return text 

