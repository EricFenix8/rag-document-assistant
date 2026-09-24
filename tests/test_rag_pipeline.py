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
        "source" in result
        for result in results
    )

    assert all(
        "score" in result
        for result in results
    )

    result = pipeline.ask(
        "What is this document about?",
        top_k=2
    )

    assert "answer" in result
    assert "sources" in result

    assert len(result["sources"]) == 2

    assert all(
        "source" in source
        for source in result["sources"]
    )

    assert all(
        "page" in source
        for source in result["sources"]
    )

    assert all(
        "score" in source
        for source in result["sources"]
    )
