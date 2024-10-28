import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

# Path to Tesseract executable (update this to your Tesseract location)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Path to the PDF file
pdf_path = r"C:\Users\Dell\Downloads\Data\Data\Samples (13).pdf"  # Replace with your PDF file path

def extract_text_from_pdf(pdf_path):
    text = ""
    # Open the PDF
    with fitz.open(pdf_path) as pdf:
        # Iterate through each page
        for page_num in range(len(pdf)):
            page = pdf[page_num]
            
            # Extract text directly from the page (useful if it's text-based)
            page_text = page.get_text()
            if page_text.strip():
                text += page_text
            else:
                # If the page has no text, it might be an image; use OCR
                pix = page.get_pixmap()  # Render page to an image
                img = Image.open(io.BytesIO(pix.tobytes("png")))  # Convert image to PIL format
                
                # Use pytesseract to extract text from the image
                page_text = pytesseract.image_to_string(img)
                text += page_text
                
            text += "\n"  # Add a newline for separation between pages
            
    return text

# Extract and print the text
pdf_text = extract_text_from_pdf(pdf_path)
print(pdf_text)
