from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Candidate(Base):
    __tablename__ = 'candidates'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True)
    phone = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    resumes = relationship("Resume", back_populates="candidate")
    match_scores = relationship("MatchScore", back_populates="candidate")

class Resume(Base):
    __tablename__ = 'resumes'
    
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    file_path = Column(String(512))
    raw_text = Column(Text)
    extracted_data = Column(JSON) # Structured data from LLM
    created_at = Column(DateTime, default=datetime.utcnow)
    
    candidate = relationship("Candidate", back_populates="resumes")

class JobDescription(Base):
    __tablename__ = 'job_descriptions'
    
    id = Column(Integer, primary_key=True)
    role_name = Column(String(255))
    raw_text = Column(Text)
    extracted_data = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    match_scores = relationship("MatchScore", back_populates="jd")

class MatchScore(Base):
    __tablename__ = 'match_scores'
    
    id = Column(Integer, primary_key=True)
    candidate_id = Column(Integer, ForeignKey('candidates.id'))
    jd_id = Column(Integer, ForeignKey('job_descriptions.id'))
    semantic_score = Column(Float)
    ranking_score = Column(Float)
    evaluation_report = Column(JSON) # Insights, skill gaps, questions
    created_at = Column(DateTime, default=datetime.utcnow)
    
    candidate = relationship("Candidate", back_populates="match_scores")
    jd = relationship("JobDescription", back_populates="match_scores")
