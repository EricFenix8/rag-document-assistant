from retriever import Retriever


documents = [
    "Python is a programming language.",
    "Python is widely used for software development.",
    "Madrid is the capital of Spain.",
    "Machine learning is a branch of artificial intelligence."
]


retriever = Retriever()

retriever.add_documents(documents)

results = retriever.search(
    "What is Python used for?",
    top_k=2
)

for document, similarity in results:
    print(f"{similarity:.4f} - {document}")