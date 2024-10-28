import pytesseract
from PIL import Image

# Set the path to tesseract.exe explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open and process the image
image_path = r"C:\Users\Dell\Downloads\Data\Data\68.jpg"  # Replace with your actual JPEG file path
image = Image.open(image_path)

# Extract text from the image
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
