from app.document_processor import DocumentProcessor


def test_document_processor():
    processor = DocumentProcessor(
        chunk_size=20,
        overlap=5
    )

    chunks = processor.process_pdf("data/sample.pdf")

    assert len(chunks) > 1
    assert all(len(chunk["text"]) > 0 for chunk in chunks)
    assert all(
        "page" in chunk
        for chunk in chunks
    )
    assert all(
    "source" in chunk
    for chunk in chunks
    )