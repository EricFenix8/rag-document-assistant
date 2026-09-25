from app.rag_pipeline import RAGPipeline


pipeline = RAGPipeline(
    chunk_size=100,
    overlap=20
)

pipeline.add_pdf("data/sample.pdf")

result = pipeline.ask(
    "What is this document about?",
    top_k=3
)


print("\nAnswer:")
print(result["answer"])

print("\nSources:")

for source in result["sources"]:
    print(
        f"- {source['source']} "
        f"(page {source['page']}, "
        f"score: {source['score']:.4f})"
    )