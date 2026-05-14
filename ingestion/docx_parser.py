import docx
import logging
import os

logger = logging.getLogger(__name__)

def extract_text_from_docx(docx_path: str) -> str:
    """
    Extracts text from a DOCX file.
    
    Args:
        docx_path (str): Path to the DOCX file.
        
    Returns:
        str: Extracted text from the DOCX.
    """
    if not os.path.exists(docx_path):
        logger.error(f"File not found: {docx_path}")
        raise FileNotFoundError(f"File not found: {docx_path}")
    
    try:
        doc = docx.Document(docx_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
    except Exception as e:
        logger.error(f"Error parsing DOCX {docx_path}: {str(e)}")
        raise Exception(f"Failed to extract text from DOCX: {str(e)}")

if __name__ == "__main__":
    # Quick test
    # print(extract_text_from_docx("sample.docx"))
    pass
