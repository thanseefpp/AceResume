import pdfplumber
import re

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file with enhanced formatting preservation.
    """
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text(x_tolerance=3, y_tolerance=3)
            text += page_text + "\n\n"  # Add extra newline to separate pages
    
    # Clean up excessive whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    
    return text.strip()

def extract_resume_sections(resume_text):
    """
    Extract sections from the resume text.
    """
    # Improved section detection
    sections = re.split(r'\n{2,}(?=[A-Z][A-Z\s]+:?$)', resume_text, flags=re.MULTILINE)
    return [section.strip() for section in sections if section.strip()]