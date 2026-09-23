import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)

    def add(self, embeddings):
        embeddings = np.asarray(embeddings, dtype="float32")
        self.index.add(embeddings)

    def search(self, query_embedding, top_k=3):
        query_embedding = np.asarray(
            query_embedding,
            dtype="float32"
        )

        scores, indices = self.index.search(
            query_embedding,
            top_k
        )

        return scores, indices