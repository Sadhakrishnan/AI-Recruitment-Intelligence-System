import re
import json
import logging
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

class ResumeData(BaseModel):
    name: str = Field(description="Full name of the candidate")
    email: str = Field(description="Email address of the candidate")
    phone: str = Field(description="Phone number of the candidate")
    links: List[str] = Field(description="Social links like LinkedIn, GitHub, etc.")
    technical_skills: List[str] = Field(description="List of technical skills")
    soft_skills: List[str] = Field(description="List of soft skills")
    education: List[Dict[str, str]] = Field(description="Education details including degree and institution")
    experience: List[Dict[str, str]] = Field(description="Work experience details including company, role, and duration")
    projects: List[Dict[str, str]] = Field(description="Project details including title and description")
    total_experience_years: float = Field(description="Total years of professional experience")

def extract_email(text: str) -> Optional[str]:
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    match = re.search(email_pattern, text)
    return match.group(0) if match else None

def extract_phone(text: str) -> Optional[str]:
    phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    match = re.search(phone_pattern, text)
    return match.group(0) if match else None

class ResumeExtractor:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)
        self.parser = PydanticOutputParser(pydantic_object=ResumeData)
        
        self.prompt = ChatPromptTemplate.from_template(
            "Extract the following information from the resume text accurately and return it in the specified JSON format.\n"
            "Resume Text:\n{resume_text}\n\n"
            "{format_instructions}"
        )

    def extract(self, text: str) -> ResumeData:
        """
        Extracts structured information from resume text using LLM.
        """
        try:
            # Basic regex extraction as backup/supplement
            email = extract_email(text)
            phone = extract_phone(text)
            
            chain = self.prompt | self.llm | self.parser
            result = chain.invoke({
                "resume_text": text,
                "format_instructions": self.parser.get_format_instructions()
            })
            
            # Fill in regex results if LLM missed them or to ensure consistency
            if not result.email and email:
                result.email = email
            if not result.phone and phone:
                result.phone = phone
                
            return result
        except Exception as e:
            logger.error(f"Error in LLM extraction: {str(e)}")
            # Fallback to a minimal object if LLM fails
            return ResumeData(
                name="Unknown",
                email=email or "Unknown",
                phone=phone or "Unknown",
                links=[],
                technical_skills=[],
                soft_skills=[],
                education=[],
                experience=[],
                projects=[],
                total_experience_years=0.0
            )

if __name__ == "__main__":
    # Example usage
    # extractor = ResumeExtractor()
    # data = extractor.extract("John Doe, email: john@example.com, Python developer with 5 years exp.")
    # print(data.json())
    pass
