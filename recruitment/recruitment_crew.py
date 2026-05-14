from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

load_dotenv()

class RecruitmentAgents:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",
            verbose=True,
            temperature=0.2,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    def resume_parser_agent(self):
        return Agent(
            role='Resume Parser Agent',
            goal='Accurately extract and structure candidate information from resumes.',
            backstory="""You are an expert technical recruiter with deep knowledge of technology stacks. 
            Your specialty is parsing complex resumes to identify key skills, experience levels, and educational backgrounds.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def ranking_agent(self):
        return Agent(
            role='Candidate Ranking Agent',
            goal='Rank candidates based on their suitability for a specific job description.',
            backstory="""You are a senior hiring manager. You evaluate candidates not just on keywords, 
            but on the depth of their experience, project relevance, and overall professional trajectory.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def skill_gap_agent(self):
        return Agent(
            role='Skill Gap Analyst Agent',
            goal='Identify missing skills in a candidate profile relative to a job description and suggest improvements.',
            backstory="""You are a career coach and technical architect. You can spot missing pieces in a 
            candidate's tech stack and provide actionable advice on how to bridge those gaps.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def interview_agent(self):
        return Agent(
            role='Interview Question Generator Agent',
            goal='Generate tailored technical and behavioral interview questions for a candidate.',
            backstory="""You are an elite technical interviewer from a top-tier tech company. 
            You know exactly what questions to ask to test both the depth of knowledge and practical problem-solving skills.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def recruiter_insight_agent(self):
        return Agent(
            role='Recruiter Insight Agent',
            goal='Provide a high-level executive summary and hiring recommendation for a candidate.',
            backstory="""You are a Chief People Officer. You provide the final word on whether a candidate 
            is a good fit for the organization, looking at cultural fit, technical prowess, and long-term potential.""",
            verbose=True,
            allow_delegation=True,
            llm=self.llm
        )
