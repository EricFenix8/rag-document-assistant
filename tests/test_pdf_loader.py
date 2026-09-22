from app.pdf_loader import PDFLoader


def test_pdf_loader():
    loader = PDFLoader()

    text = loader.load("data/sample.pdf")

    assert len(text) > 0