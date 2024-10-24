import fitz  # PyMuPDF
import re


# Step 1: Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page_num in range(doc.page_count):
            page = doc.load_page(page_num)
            page_text = page.get_text()
            text += page_text
    return text


# Step 2: Clean the Extracted Text
def clean_text(text):
    # Remove extra whitespaces and newlines
    text = " ".join(text.split())
    # Remove non-ASCII characters
    text = text.encode("ascii", "ignore").decode()
    # Remove special characters (optional)
    text = re.sub(r"[^\w\s.,;:!?()-]", "", text)
    # Convert text to lowercase (optional)
    text = text.lower()
    return text


# Example Usage
pdf_path = "data/User Manual.pdf"  # Replace with your PDF file path
raw_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(raw_text)

# (Optional) Save the Cleaned Text
with open("cleaned_car_manual.txt", "w", encoding="utf-8") as f:
    f.write(cleaned_text)
