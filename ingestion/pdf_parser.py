import fitz  # PyMuPDF
import logging
import os

logger = logging.getLogger(__name__)

def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file using PyMuPDF.
    
    Args:
        pdf_path (str): Path to the PDF file.
        
    Returns:
        str: Extracted text from the PDF.
    """
    if not os.path.exists(pdf_path):
        logger.error(f"File not found: {pdf_path}")
        raise FileNotFoundError(f"File not found: {pdf_path}")
    
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        logger.error(f"Error parsing PDF {pdf_path}: {str(e)}")
        raise Exception(f"Failed to extract text from PDF: {str(e)}")
    
    return text

if __name__ == "__main__":
    # Quick test
    # print(extract_text_from_pdf("sample.pdf"))
    pass
