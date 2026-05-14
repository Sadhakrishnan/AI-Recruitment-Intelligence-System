import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import logging
from typing import List, Dict, Union

logger = logging.getLogger(__name__)

class SemanticMatcher:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initializes the SemanticMatcher with a pre-trained model.
        Default is 'all-MiniLM-L6-v2' for a good balance of speed and accuracy.
        """
        try:
            self.model = SentenceTransformer(model_name)
            logger.info(f"Loaded embedding model: {model_name}")
        except Exception as e:
            logger.error(f"Error loading embedding model: {str(e)}")
            raise e

    def get_embeddings(self, texts: Union[str, List[str]]) -> np.ndarray:
        """
        Generates embeddings for a single text or a list of texts.
        """
        return self.model.encode(texts)

    def compute_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        """
        Computes cosine similarity between two embeddings.
        """
        # Ensure they are 2D arrays for cosine_similarity
        if embedding1.ndim == 1:
            embedding1 = embedding1.reshape(1, -1)
        if embedding2.ndim == 1:
            embedding2 = embedding2.reshape(1, -1)
            
        return float(cosine_similarity(embedding1, embedding2)[0][0])

    def rank_candidates(self, jd_embedding: np.ndarray, candidate_embeddings: List[np.ndarray]) -> List[float]:
        """
        Ranks candidates by computing similarity to a JD embedding.
        """
        scores = []
        for cand_emb in candidate_embeddings:
            scores.append(self.compute_similarity(jd_embedding, cand_emb))
        return scores

if __name__ == "__main__":
    # Example usage
    # matcher = SemanticMatcher()
    # jd = "Python developer with experience in FastAPI and LLMs"
    # resume = "Experienced backend engineer specialized in Python and AI pipelines."
    # jd_emb = matcher.get_embeddings(jd)
    # res_emb = matcher.get_embeddings(resume)
    # print(f"Similarity: {matcher.compute_similarity(jd_emb, res_emb)}")
    pass
