import streamlit as st
import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(
    page_title="AI Recruitment Intelligence",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 AI Recruitment Intelligence Copilot")
st.markdown("---")

tabs = st.tabs(["📂 Resume Ingestion", "📝 Job Description", "📊 Candidate Ranking", "🧠 AI Insights", "📈 Analytics"])

# 1. Resume Ingestion Tab
with tabs[0]:
    st.header("Upload Resumes")
    uploaded_files = st.file_uploader("Choose PDF or DOCX files", accept_multiple_files=True)
    
    if st.button("Process Resumes"):
        if uploaded_files:
            for file in uploaded_files:
                with st.spinner(f"Processing {file.name}..."):
                    files = {"file": (file.name, file.getvalue())}
                    response = requests.post(f"{API_URL}/upload_resume", files=files)
                    if response.status_code == 200:
                        st.success(f"Successfully processed {file.name}")
                        st.json(response.json())
                    else:
                        st.error(f"Failed to process {file.name}: {response.text}")
        else:
            st.warning("Please upload at least one resume.")

# 2. Job Description Tab
with tabs[1]:
    st.header("Define Job Role")
    jd_text = st.text_area("Paste Job Description here...", height=300)
    
    if st.button("Analyze JD"):
        if jd_text:
            with st.spinner("Analyzing Job Description..."):
                response = requests.post(f"{API_URL}/upload_job", params={"jd_text": jd_text})
                if response.status_code == 200:
                    st.success("JD Analyzed Successfully")
                    data = response.json()["extracted_info"]
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Key Requirements")
                        st.write(f"**Role:** {data['role_name']}")
                        st.write(f"**Min Exp:** {data['min_experience_years']} years")
                        st.write(f"**Seniority:** {data['seniority_level']}")
                    with col2:
                        st.subheader("Required Skills")
                        st.write(", ".join(data['required_skills']))
                else:
                    st.error("Failed to analyze JD.")
        else:
            st.warning("Please paste a job description.")

# 3. Candidate Ranking Tab
with tabs[2]:
    st.header("Ranked Candidates")
    search_query = st.text_input("Search candidates (e.g., 'Python developer with RAG experience')")
    
    if st.button("Search & Rank"):
        with st.spinner("Searching..."):
            response = requests.get(f"{API_URL}/search_candidates", params={"query": search_query})
            if response.status_code == 200:
                results = response.json()["results"]
                if results:
                    df = pd.DataFrame(results)
                    st.table(df[["name", "email", "score"]])
                else:
                    st.info("No candidates found matching the query.")
            else:
                st.error("Search failed.")

# Placeholder for other tabs
with tabs[3]:
    st.info("Multi-agent evaluation insights will appear here after selection.")

with tabs[4]:
    st.info("Hiring analytics and skill demand heatmaps will appear here.")
