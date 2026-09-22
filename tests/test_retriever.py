from app.retriever import Retriever


def test_retriever():
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

    assert len(results) == 2
    assert results[0][0] == "Python is a programming language."