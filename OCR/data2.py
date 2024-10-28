import pytesseract
from PIL import Image
import os
import pandas as pd

# Set the path to tesseract.exe explicitly
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the folder path containing the images and the output Excel file path
folder_path = r"C:\Users\Dell\Desktop\JPEG Data"  # Replace with your folder path
output_excel_path = r"C:\Users\Dell\Desktop\JPEG Data\extracted_text.xlsx"  # Path to save Excel file

# Create an empty list to store extracted data
data = []

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a JPEG image
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
        # Create the full file path
        file_path = os.path.join(folder_path, filename)
        
        # Open and process the image
        image = Image.open(file_path)
        
        # Extract text from the image
        text = pytesseract.image_to_string(image)
        
        # Append filename and text to the data list
        data.append({"Filename": filename, "Extracted Text": text})

# Create a DataFrame from the data list
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel(output_excel_path, index=False)

print(f"Text extracted and saved to {output_excel_path}")
