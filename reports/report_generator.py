from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os
import logging

logger = logging.getLogger(__name__)

class ReportGenerator:
    def __init__(self, output_dir: str = "data/reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.styles = getSampleStyleSheet()

    def generate_candidate_report(self, candidate_data: dict, evaluation_data: dict) -> str:
        """
        Generates a PDF report for a specific candidate evaluation.
        """
        file_name = f"{candidate_data['name'].replace(' ', '_')}_Evaluation.pdf"
        file_path = os.path.join(self.output_dir, file_name)
        
        doc = SimpleDocTemplate(file_path, pagesize=letter)
        elements = []

        # Title
        title_style = self.styles['Heading1']
        elements.append(Paragraph(f"Recruitment Evaluation: {candidate_data['name']}", title_style))
        elements.append(Spacer(1, 12))

        # Basic Info Table
        info_data = [
            ["Email", candidate_data.get('email', 'N/A')],
            ["Phone", candidate_data.get('phone', 'N/A')],
            ["Score", str(evaluation_data.get('score', 'N/A')) + "/100"]
        ]
        t = Table(info_data, colWidths=[100, 300])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
        ]))
        elements.append(t)
        elements.append(Spacer(1, 20))

        # Insights
        elements.append(Paragraph("AI Recruiter Insights", self.styles['Heading2']))
        elements.append(Paragraph(evaluation_data.get('insights', 'No insights available.'), self.styles['BodyText']))
        elements.append(Spacer(1, 12))

        # Skill Gaps
        elements.append(Paragraph("Skill Gap Analysis", self.styles['Heading2']))
        gaps = evaluation_data.get('skill_gaps', [])
        if gaps:
            for gap in gaps:
                elements.append(Paragraph(f"• {gap}", self.styles['BodyText']))
        else:
            elements.append(Paragraph("No significant skill gaps identified.", self.styles['BodyText']))
        elements.append(Spacer(1, 12))

        # Interview Questions
        elements.append(Paragraph("Recommended Interview Questions", self.styles['Heading2']))
        questions = evaluation_data.get('interview_questions', [])
        for q in questions:
            elements.append(Paragraph(f"Q: {q}", self.styles['BodyText']))
            elements.append(Spacer(1, 6))

        try:
            doc.build(elements)
            logger.info(f"Report generated: {file_path}")
            return file_path
        except Exception as e:
            logger.error(f"Error building PDF: {str(e)}")
            raise e

if __name__ == "__main__":
    # Example usage
    # generator = ReportGenerator()
    # cand = {"name": "John Doe", "email": "john@example.com"}
    # eval = {"score": 85, "insights": "Solid candidate.", "skill_gaps": ["Docker"], "interview_questions": ["Explain Docker."]}
    # generator.generate_candidate_report(cand, eval)
    pass
