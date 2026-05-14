import sys
import os
import unittest

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ingestion.pdf_parser import extract_text_from_pdf
from extraction.resume_extractor import ResumeExtractor
from embeddings.semantic_matcher import SemanticMatcher

class TestRecruitmentSystem(unittest.TestCase):
    
    def test_semantic_matcher(self):
        matcher = SemanticMatcher()
        text1 = "Python developer"
        text2 = "Software engineer specialized in Python"
        text3 = "Expert chef in Italian cuisine"
        
        emb1 = matcher.get_embeddings(text1)
        emb2 = matcher.get_embeddings(text2)
        emb3 = matcher.get_embeddings(text3)
        
        sim12 = matcher.compute_similarity(emb1, emb2)
        sim13 = matcher.compute_similarity(emb1, emb3)
        
        print(f"Similarity (Python vs Python): {sim12}")
        print(f"Similarity (Python vs Chef): {sim13}")
        
        self.assertGreater(sim12, sim13, "Semantic similarity failed to distinguish relevant texts.")

    def test_resume_extractor_mock(self):
        # We won't call the actual LLM here to avoid API costs during unit tests
        # Just testing the regex and pydantic structure
        from extraction.resume_extractor import ResumeData, extract_email
        
        text = "Contact me at john.doe@example.com or call 123-456-7890."
        email = extract_email(text)
        self.assertEqual(email, "john.doe@example.com")

if __name__ == "__main__":
    unittest.main()
