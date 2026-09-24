from app.retriever import Retriever


def test_retriever():
    chunks = [
        {
            "text": "Python is a programming language.",
            "page": 1,
            "source": "test.pdf"
        },
        {
            "text": "Python is widely used for software development.",
            "page": 2,
            "source": "test.pdf"
        },
        {
            "text": "Madrid is the capital of Spain.",
            "page": 3,
            "source": "test.pdf"
        },
        {
            "text": "Machine learning is a branch of artificial intelligence.",
            "page": 4,
            "source": "test.pdf"
        }
    ]

    retriever = Retriever()

    retriever.add_documents(chunks)

    results = retriever.search(
        "What is Python used for?",
        top_k=2
    )

    assert len(results) == 2

    assert results[0]["text"] == \
        "Python is a programming language."

    assert "page" in results[0]
    assert "score" in results[0]