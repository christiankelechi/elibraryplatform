# import json
# from PyPDF2 import PdfReader
# def append_to_json(json_file, text_data):
#     with open(json_file, 'a') as f:
#         json.dump(text_data, f)
#         f.write('\n')  # Add a newline to separate entries

# def pdf_to_json(pdf_path,json_file):
#     reader = PdfReader(pdf_path)
#     for i,page in enumerate(reader.pages):
#         current_page_text=page.extract_text()
#         data = {"page": i + 1, "text": current_page_text}
#         append_to_json(json_file, data)
# pdf_path = "mypython.pdf"
# json_file = "pdf_text.json"
# pdf_to_json(pdf_path, json_file)