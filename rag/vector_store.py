import faiss
import numpy as np
import os
import pickle
import logging
from typing import List, Dict, Any, Optional

logger = logging.getLogger(__name__)

class VectorStore:
    def __init__(self, dimension: int = 384, index_path: str = "data/faiss_index.bin"):
        """
        Initializes a FAISS vector store.
        Default dimension 384 corresponds to all-MiniLM-L6-v2.
        """
        self.dimension = dimension
        self.index_path = index_path
        self.metadata_path = index_path.replace(".bin", "_metadata.pkl")
        
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.metadata_path, 'rb') as f:
                self.metadata = pickle.load(f)
            logger.info(f"Loaded existing FAISS index from {self.index_path}")
        else:
            self.index = faiss.IndexFlatIP(dimension) # Inner Product similarity (cosine if normalized)
            self.metadata = []
            logger.info("Created new FAISS index")

    def add_vectors(self, vectors: np.ndarray, metadata: List[Dict[str, Any]]):
        """
        Adds vectors and their corresponding metadata to the store.
        """
        if vectors.shape[1] != self.dimension:
            raise ValueError(f"Vector dimension {vectors.shape[1]} does not match index dimension {self.dimension}")
        
        # Normalize vectors for cosine similarity (IndexFlatIP + normalization = cosine)
        faiss.normalize_L2(vectors)
        self.index.add(vectors)
        self.metadata.extend(metadata)
        self.save()

    def search(self, query_vector: np.ndarray, k: int = 5) -> List[Dict[str, Any]]:
        """
        Searches for the top k similar vectors.
        """
        if query_vector.shape[1] != self.dimension:
            query_vector = query_vector.reshape(1, -1)
        
        faiss.normalize_L2(query_vector)
        distances, indices = self.index.search(query_vector, k)
        
        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx != -1 and idx < len(self.metadata):
                item = self.metadata[idx].copy()
                item['score'] = float(dist)
                results.append(item)
        
        return results

    def save(self):
        """
        Persists the index and metadata to disk.
        """
        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, 'wb') as f:
            pickle.dump(self.metadata, f)
        logger.info(f"Saved FAISS index to {self.index_path}")

if __name__ == "__main__":
    # Example usage
    # store = VectorStore()
    # vectors = np.random.random((5, 384)).astype('float32')
    # meta = [{"id": i, "name": f"Candidate {i}"} for i in range(5)]
    # store.add_vectors(vectors, meta)
    # query = np.random.random((1, 384)).astype('float32')
    # print(store.search(query, k=2))
    pass
