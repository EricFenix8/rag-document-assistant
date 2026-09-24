from app.rag_pipeline import RAGPipeline


def test_rag_pipeline():

    pipeline = RAGPipeline(
        chunk_size=20,
        overlap=5
    )

    pipeline.add_pdf("data/sample.pdf")

    results = pipeline.search(
        "What is this document about?",
        top_k=2
    )

    assert len(results) == 2

    assert all(
        len(result["text"]) > 0
        for result in results
    )

    assert all(
        "page" in result
        for result in results
    )

    assert all(
        "score" in result
        for result in results
    )