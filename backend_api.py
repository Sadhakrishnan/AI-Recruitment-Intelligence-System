from fastapi import FastAPI, UploadFile, File, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
import logging
from typing import List, Optional
from datetime import datetime
from dotenv import load_dotenv

# Internal imports
from ingestion.pdf_parser import extract_text_from_pdf
from ingestion.docx_parser import extract_text_from_docx
from extraction.resume_extractor import ResumeExtractor
from extraction.jd_extractor import JDExtractor
from embeddings.semantic_matcher import SemanticMatcher
from rag.vector_store import VectorStore
# (Database imports will be added when DB is fully configured)

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Recruitment Intelligence API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
resume_extractor = ResumeExtractor()
jd_extractor = JDExtractor()
matcher = SemanticMatcher()
vector_store = VectorStore()

UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "AI Recruitment Intelligence System is online."}

@app.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # 1. Extract Text
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file.filename.endswith(".docx"):
            text = extract_text_from_docx(file_path)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file format")
        
        # 2. Extract Structured Data
        extracted_data = resume_extractor.extract(text)
        
        # 3. Generate Embedding & Store
        embedding = matcher.get_embeddings(text)
        vector_store.add_vectors(
            np_array_from_embedding(embedding), # Helper needed
            [{"name": extracted_data.name, "email": extracted_data.email, "filename": file.filename}]
        )
        
        return {
            "status": "success",
            "filename": file.filename,
            "candidate_name": extracted_data.name,
            "extracted_info": extracted_data.dict()
        }
    except Exception as e:
        logger.error(f"Error processing resume: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload_job")
async def upload_job(jd_text: str):
    try:
        extracted_jd = jd_extractor.extract(jd_text)
        return {
            "status": "success",
            "role_name": extracted_jd.role_name,
            "extracted_info": extracted_jd.dict()
        }
    except Exception as e:
        logger.error(f"Error processing JD: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/search_candidates")
async def search_candidates(query: str, k: int = 5):
    try:
        query_embedding = matcher.get_embeddings(query)
        results = vector_store.search(query_embedding, k=k)
        return {"results": results}
    except Exception as e:
        logger.error(f"Error searching candidates: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

def np_array_from_embedding(embedding):
    import numpy as np
    return np.array([embedding]).astype('float32')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
