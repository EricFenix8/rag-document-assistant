from app.embeddings import EmbeddingModel
from app.vector_store import VectorStore


class Retriever:

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.embedding_model = EmbeddingModel(model_name)
        self.vector_store = None
        self.chunks = []

    def add_documents(self, chunks):
        self.chunks = chunks

        texts = [chunk["text"] for chunk in chunks]

        embeddings = self.embedding_model.encode(texts)

        dimension = embeddings.shape[1]

        self.vector_store = VectorStore(dimension)
        self.vector_store.add(embeddings)

    #Devuelve los chunks mas importantes para una consulta junto a su metadata y puntuacion de similitud
    def search(self, query, top_k=3):
        query_embedding = self.embedding_model.encode([query])

        scores, indices = self.vector_store.search(
            query_embedding,
            top_k
        )

        results = []

        for score, index in zip(scores[0], indices[0]):
            chunk = self.chunks[index]

            results.append({
                "text": chunk["text"],
                "page": chunk["page"],
                "score": float(score)
            })

        return results