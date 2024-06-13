import fitz  # PyMuPDF

# Directory where the PDF file is stored
pdf_file = r'C:\Users\new\Downloads\Internship-Report updated.pdf'
# Directory where the text file will be saved
txt_file = r'C:\Users\new\Downloads\Internship-Report updated.txt'

def pdf_to_text(pdf_path, txt_path):
    """Convert PDF to text and save to a text file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    with open(txt_path, 'w', encoding='utf-8') as f:
        f.write(text)

pdf_to_text(pdf_file, txt_file)
print(f"Converted {pdf_file} to {txt_file}")

