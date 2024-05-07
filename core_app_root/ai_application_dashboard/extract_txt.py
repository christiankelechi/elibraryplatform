import re
import json
from PyPDF2 import PdfReader

def remove_special_symbols(text):
    # Define a regular expression pattern to match non-alphanumeric characters
    pattern = r'[^a-zA-Z0-9\s]'
    # Use the sub() method to replace all non-alphanumeric characters with an empty string
    return re.sub(pattern, '', text)

def append_to_json(json_file, text_data):
    with open(json_file, 'w') as f:
        json.dump(text_data, f, indent=4)  # Adding indentation for better readability
        f.write('\n')  # Add a newline to separate entries

def pdf_to_json(pdf_path, json_file):
    reader = PdfReader(pdf_path)
    full_text = ""  # Initialize an empty string to store the text from all pages
    for i, page in enumerate(reader.pages):
        # if i==30:
        #     break
        current_page_text = page.extract_text()
        full_text += current_page_text  # Append the text from the current page to the full text
    
    # Remove special symbols from the full text
    clean_text = remove_special_symbols(full_text)
    
    data = {"text": clean_text}  # Store the cleaned text under the key "text"
    append_to_json(json_file, data)

# Usage
# pdf_path = "mypython.pdf"
# json_file = "pdf_text.json"
# pdf_to_json(pdf_path, json_file)
