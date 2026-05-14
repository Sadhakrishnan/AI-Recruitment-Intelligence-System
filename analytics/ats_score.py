import re
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class ATSScorer:
    def __init__(self):
        # Keywords that often indicate good resume structure
        self.essential_sections = [
            "experience", "education", "skills", "projects", "contact", "summary"
        ]

    def score_resume(self, resume_text: str, jd_skills: List[str]) -> Dict[str, Any]:
        """
        Calculates an ATS score (0-100) based on multiple factors.
        """
        score = 0
        details = []
        
        # 1. Section Completeness (30 points)
        found_sections = []
        for section in self.essential_sections:
            if re.search(rf"\b{section}\b", resume_text, re.IGNORECASE):
                found_sections.append(section)
        
        section_score = (len(found_sections) / len(self.essential_sections)) * 30
        score += section_score
        details.append(f"Found {len(found_sections)}/{len(self.essential_sections)} essential sections (+{int(section_score)})")

        # 2. Keyword Matching (40 points)
        if jd_skills:
            matched_skills = []
            for skill in jd_skills:
                if re.search(rf"\b{re.escape(skill)}\b", resume_text, re.IGNORECASE):
                    matched_skills.append(skill)
            
            skill_score = (len(matched_skills) / len(jd_skills)) * 40 if jd_skills else 0
            score += skill_score
            details.append(f"Matched {len(matched_skills)}/{len(jd_skills)} required skills (+{int(skill_score)})")
        else:
            details.append("No JD skills provided for matching (+0)")

        # 3. Formatting & Readability (30 points)
        # Check for measurable achievements (numbers/percentages)
        has_metrics = len(re.findall(r"\d+%", resume_text)) > 0 or len(re.findall(r"\$\d+", resume_text)) > 0
        if has_metrics:
            score += 15
            details.append("Includes measurable achievements (+15)")
        else:
            details.append("Missing measurable achievements (e.g., % or $ improvements) (+0)")
            
        # Check for length (reasonable text length)
        if 500 < len(resume_text) < 10000:
            score += 15
            details.append("Resume length is optimal (+15)")
        else:
            details.append("Resume might be too short or too long (+0)")

        return {
            "overall_score": int(score),
            "breakdown": details,
            "missing_sections": list(set(self.essential_sections) - set(found_sections))
        }

if __name__ == "__main__":
    # Example usage
    # scorer = ATSScorer()
    # result = scorer.score_resume("John Doe Experience: 5 years Python...", ["Python", "FastAPI"])
    # print(result)
    pass
