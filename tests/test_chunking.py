from app.chunking import TextChunker


def test_chunking():
    text = """
    Python is a programming language widely used in software development.
    It is also popular in data science and machine learning.
    Machine learning is a branch of artificial intelligence.
    Artificial intelligence allows computers to perform tasks that normally require human intelligence.
    """

    chunker = TextChunker(
        chunk_size=20,
        overlap=5
    )

    chunks = chunker.split(text)

    assert len(chunks) > 1
    assert all(len(chunk) > 0 for chunk in chunks)