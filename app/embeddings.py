from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "Python is a programming language.",
    "Python is widely used for software development.",
    "Madrid is the capital of Spain."
]

embeddings = model.encode(texts)

question = "What is Python used for?"

question_embedding = model.encode([question])

similarities = cosine_similarity(question_embedding, embeddings)[0]

for text, similarity in zip(texts, similarities):
    print(f"{similarity:.4f} - {text}")