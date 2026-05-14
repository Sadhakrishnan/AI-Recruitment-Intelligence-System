# AI Recruitment Intelligence System

An enterprise-grade AI-powered recruitment intelligence and candidate evaluation platform that uses semantic embeddings, multi-agent reasoning, recruiter intelligence, RAG-powered search, and explainable ranking systems to automate modern hiring workflows.

---

## 🚀 Features

* Resume parsing and structured extraction
* Job description understanding
* Semantic candidate-job matching
* AI-powered candidate ranking
* Skill-gap analysis
* ATS resume scoring
* Interview question generation
* Recruiter insight generation
* RAG-powered talent search
* Multi-agent evaluation workflows
* Analytics dashboard
* Downloadable recruiter reports

---

## 🎯 Project Goal

The system can:

✅ Parse resumes automatically from PDF/DOCX/TXT
✅ Extract candidate skills, experience, projects, and education
✅ Understand job descriptions semantically
✅ Match candidates using embedding similarity
✅ Rank applicants intelligently using weighted scoring
✅ Detect missing skills and generate learning recommendations
✅ Generate adaptive interview questions
✅ Provide recruiter-style hiring insights
✅ Support semantic recruiter search using RAG
✅ Generate professional hiring reports and analytics

### Example Output

```
{
  "candidate": "John Doe",
  "semantic_score": 0.91,
  "rank_score": 94,
  "missing_skills": ["Kubernetes", "Docker"],
  "hire_recommendation": "Strong Match",
  "interview_questions": [
    "Explain how vector databases improve retrieval in RAG systems."
  ],
  "recruiter_insight": "Strong AI backend engineering profile with excellent RAG project experience but limited DevOps exposure."
}
```

---

## 🧠 System Architecture

```
Resume PDFs + Job Descriptions
            ↓
Document Parsing Pipeline
            ↓
Information Extraction Engine
            ↓
Embedding + Semantic Similarity Engine
            ↓
Candidate Ranking System
            ↓
Multi-Agent Evaluation Layer
 ├── Resume Parser Agent
 ├── Semantic Matching Agent
 ├── Skill Gap Agent
 ├── Candidate Ranking Agent
 ├── Interview Question Agent
 ├── Recruiter Insight Agent
 ├── ATS Analysis Agent
            ↓
LLM Reasoning + Recommendations
            ↓
Dashboard + Reports + Search Interface
```

---

## 🛠️ Tech Stack

### NLP / Embeddings

* Sentence Transformers
* HuggingFace Transformers
* BGE Embeddings
* all-MiniLM-L6-v2
* spaCy

### Vector Database / RAG

* FAISS
* ChromaDB

### Multi-Agent Framework

* LangChain
* CrewAI

### Backend

* FastAPI

### Frontend

* Streamlit
* React

### Database

* PostgreSQL

### AI / LLM

* OpenAI GPT
* Mistral
* LLaMA

### Document Processing

* PyMuPDF
* pdfplumber
* python-docx
* Tesseract OCR
* EasyOCR

---

## 📄 Resume Ingestion Pipeline

Supports:

* PDF resumes
* DOCX resumes
* TXT resumes
* Batch uploads
* OCR for scanned resumes

Capabilities:

* File validation
* Text extraction
* Metadata handling
* Parsing error handling
* Batch processing

---

## 🔍 Resume Parsing Engine

Extracts:

* Candidate name
* Email and phone number
* LinkedIn/GitHub profiles
* Technical skills
* Soft skills
* Education details
* Certifications
* Projects
* Work experience
* Years of experience
* Technologies used

Uses:

* spaCy NER
* Regex extraction
* LLM-based structured extraction

Example:

```
{
  "name": "John Doe",
  "skills": ["Python", "FastAPI", "PyTorch"],
  "experience_years": 3,
  "projects": ["RAG chatbot", "OCR pipeline"]
}
```

---

## 🧠 Job Description Understanding Engine

Extracts:

* Required skills
* Preferred skills
* Experience requirements
* Responsibilities
* Tools/frameworks
* Domain knowledge
* Soft skills

Features:

* Mandatory vs optional skill detection
* Seniority classification
* Technology stack extraction
* Role category inference

Example:

```
{
  "required_skills": ["Python", "LangChain", "RAG"],
  "experience_required": 2
}
```

---

## 🔥 Semantic Matching Engine

Core AI matching system using embeddings.

Uses:

* Sentence Transformers
* Cosine similarity
* Semantic embeddings
* Vector search

Understands semantic similarity:

```
Generative AI ≈ LLM Systems ≈ RAG Pipelines
```

Vector Storage:

* FAISS
* ChromaDB

Example:

```
{
  "candidate": "John Doe",
  "semantic_score": 0.89
}
```

---

## 📊 Candidate Ranking Engine

Ranks candidates using:

* Semantic similarity
* Skill overlap
* Project relevance
* Experience level
* Domain alignment
* Certification relevance

Features:

* Weighted scoring
* Recruiter-adjustable priorities
* Explainable ranking logic

---

## 🧩 Skill Gap Detection Agent

Detects:

* Missing skills
* Weak skill areas
* Learning gaps

Generates:

* Learning roadmaps
* Certification suggestions
* Project recommendations
* Improvement strategies

Example:

```
Missing Skills:
- Kubernetes
- Docker
- LangChain
```

---

## 🎤 Interview Question Generation Agent

Generates:

* Technical interview questions
* Coding questions
* Behavioral questions
* Scenario-based questions
* Project-based questions

Adaptive based on:

* Candidate skills
* Job role
* Seniority level

---

## 🧠 Recruiter Insight Agent

Provides:

* Candidate strengths
* Weaknesses
* Project quality analysis
* Career trajectory insights
* Role suitability assessment
* Hire recommendations
* Confidence score

Example:

> Strong backend AI engineering experience with excellent RAG system development but limited cloud deployment exposure.

---

## 📈 ATS Resume Scoring System

Analyzes:

* Resume formatting quality
* Keyword optimization
* Readability
* Section structure
* Missing information

Output:

```
ATS Score: 84/100
```

---

## 🔍 RAG-Powered Talent Search

Example recruiter query:

```
Find candidates with OCR and computer vision experience.
```

Flow:

```
Recruiter Query
        ↓
Embedding Search
        ↓
Semantic Retrieval
        ↓
Ranked Candidate Results
```

---

## 🤖 Multi-Agent Architecture

Agents:

* Resume Parser Agent
* Semantic Matching Agent
* Ranking Agent
* Skill Gap Agent
* Interview Agent
* Recruiter Insight Agent
* ATS Analysis Agent

Features:

* Shared memory
* Collaborative reasoning
* Context passing
* Iterative evaluation

---

## 📊 Analytics Dashboard

Features:

* Candidate ranking table
* Match score visualization
* Skill-gap charts
* Hiring analytics
* Recruiter AI insights
* Resume preview
* Candidate comparison
* Search filters
* Interactive graphs

---

## 🌐 Backend API

Endpoints:

* POST /upload_resume
* POST /upload_job
* GET /rank_candidates
* GET /skill_gap
* POST /generate_questions
* POST /search_candidates
* GET /analytics
* GET /report

---

## 🗄️ Database Design

PostgreSQL tables:

* candidates
* resumes
* skills
* job_descriptions
* match_scores
* interview_questions
* recruiter_feedback
---

## ⚙️ Installation

```
git clone https://github.com/your-username/ai-recruitment-intelligence.git
cd ai-recruitment-intelligence
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start backend:

```
uvicorn api.main:app --reload
```

Launch dashboard:

```
streamlit run frontend/dashboard.py
```

---

## 📥 Report Generation

Generates:

* PDF reports
* DOCX recruiter reports

Includes:

* Candidate ranking
* Strengths and weaknesses
* ATS score
* Skill gaps
* Interview questions
* Recruiter recommendations

---

## 🔥 Advanced Features

* Hiring bias detection
* Fairness analysis
* Voice interview analysis
* AI resume rewrite suggestions
* Candidate clustering
* Salary estimation
* Recruiter copilot chat assistant
* Hiring trend analytics
* Confidence-based recommendations

---

## 📊 Metrics

* Semantic retrieval accuracy
* Ranking quality
* Candidate-job similarity
* ATS scoring quality
* Skill-gap precision
* Recruiter satisfaction metrics


