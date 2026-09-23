from app.document_processor import DocumentProcessor


def test_document_processor():
    processor = DocumentProcessor(
        chunk_size=20,
        overlap=5
    )

    chunks = processor.process_pdf("data/sample.pdf")

    assert len(chunks) > 1
    assert all(len(chunk) > 0 for chunk in chunks)