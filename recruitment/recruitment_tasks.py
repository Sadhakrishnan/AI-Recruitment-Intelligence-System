from crewai import Task
from typing import Dict, Any

class RecruitmentTasks:
    def parsing_task(self, agent, resume_text):
        return Task(
            description=f"Parse the following resume text and extract structured information including skills, experience, and education.\n\nResume Text:\n{resume_text}",
            agent=agent,
            expected_output="A structured JSON-like summary of the candidate's profile."
        )

    def ranking_task(self, agent, candidate_summary, jd_text):
        return Task(
            description=f"Evaluate the candidate based on the following summary and job description. Provide a ranking score (0-100) and justification.\n\nCandidate Summary:\n{candidate_summary}\n\nJob Description:\n{jd_text}",
            agent=agent,
            expected_output="A ranking score and a detailed explanation of the score."
        )

    def skill_gap_task(self, agent, candidate_summary, jd_text):
        return Task(
            description=f"Identify the skill gaps between the candidate and the job description. Suggest learning paths.\n\nCandidate Summary:\n{candidate_summary}\n\nJob Description:\n{jd_text}",
            agent=agent,
            expected_output="A list of missing skills and specific recommendations for improvement."
        )

    def interview_task(self, agent, candidate_summary, jd_text):
        return Task(
            description=f"Generate 5 technical and 3 behavioral interview questions tailored to this candidate for this specific role.\n\nCandidate Summary:\n{candidate_summary}\n\nJob Description:\n{jd_text}",
            agent=agent,
            expected_output="A list of 8 tailored interview questions with brief explanations of why they are being asked."
        )

    def insight_task(self, agent, candidate_summary, ranking_result, skill_gap_result):
        return Task(
            description=f"Synthesize all the evaluations to provide a final recruiter insight report.\n\nCandidate Summary:\n{candidate_summary}\n\nRanking Result:\n{ranking_result}\n\nSkill Gap Result:\n{skill_gap_result}",
            agent=agent,
            expected_output="A comprehensive recruiter insight report including strengths, weaknesses, and a final 'Hire/No Hire' recommendation."
        )
