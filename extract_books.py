import fitz  # PyMuPDF

def extract_all_content(pdf_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

pdf_path = "mypdf.pdf"
all_content = extract_all_content(pdf_path)
print(all_content)
