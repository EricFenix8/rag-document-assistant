from app.rag_pipeline import RAGPipeline


pipeline = RAGPipeline(
    chunk_size=100,
    overlap=20
)

pipeline.add_pdf("data/sample.pdf")

results = pipeline.search(
    "What is this document about?",
    top_k=5
)

for document, score in results:
    print(f"\nScore: {score:.4f}")
    print(document[:300])