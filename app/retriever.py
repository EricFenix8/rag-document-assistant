from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class Retriever:

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.documents = []
        self.embeddings = None

    def add_documents(self, documents):
        self.documents = documents
        self.embeddings = self.model.encode(documents)

    def search(self, query, top_k=3):
        query_embedding = self.model.encode([query])

        similarities = cosine_similarity(
            query_embedding,
            self.embeddings
        )[0]

        results = sorted(
            zip(self.documents, similarities),
            key=lambda x: x[1],
            reverse=True
        )

        return results[:top_k]