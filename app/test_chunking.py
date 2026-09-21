from chunking import TextChunker


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

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i + 1} ---")
    print(chunk)