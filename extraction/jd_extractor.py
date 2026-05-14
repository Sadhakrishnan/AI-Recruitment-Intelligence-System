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

class JDData(BaseModel):
    role_name: str = Field(description="Title of the job role")
    required_skills: List[str] = Field(description="List of mandatory technical skills")
    preferred_skills: List[str] = Field(description="List of optional or preferred skills")
    min_experience_years: float = Field(description="Minimum years of experience required")
    responsibilities: List[str] = Field(description="Key responsibilities of the role")
    education_required: Optional[str] = Field(description="Educational requirements")
    technology_stack: List[str] = Field(description="Key technologies and frameworks used")
    seniority_level: str = Field(description="Seniority level (e.g., Junior, Mid, Senior, Lead)")

class JDExtractor:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=0)
        self.parser = PydanticOutputParser(pydantic_object=JDData)
        
        self.prompt = ChatPromptTemplate.from_template(
            "Extract the following information from the job description text accurately and return it in the specified JSON format.\n"
            "Job Description Text:\n{jd_text}\n\n"
            "{format_instructions}"
        )

    def extract(self, text: str) -> JDData:
        """
        Extracts structured information from JD text using LLM.
        """
        try:
            chain = self.prompt | self.llm | self.parser
            result = chain.invoke({
                "jd_text": text,
                "format_instructions": self.parser.get_format_instructions()
            })
            return result
        except Exception as e:
            logger.error(f"Error in LLM JD extraction: {str(e)}")
            return JDData(
                role_name="Unknown",
                required_skills=[],
                preferred_skills=[],
                min_experience_years=0.0,
                responsibilities=[],
                education_required="Unknown",
                technology_stack=[],
                seniority_level="Unknown"
            )

if __name__ == "__main__":
    # Example usage
    # extractor = JDExtractor()
    # data = extractor.extract("Looking for a Senior Python Developer with 5+ years of exp in FastAPI.")
    # print(data.json())
    pass
