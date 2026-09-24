from app.pdf_loader import PDFLoader
from app.chunking import TextChunker


class DocumentProcessor:

    def __init__(self, chunk_size=100, overlap=20):
        self.pdf_loader = PDFLoader()
        self.chunker = TextChunker(
            chunk_size=chunk_size,
            overlap=overlap
        )

    def process_pdf(self, file_path):
        pages = self.pdf_loader.load(file_path)

        chunks = self.chunker.split_pages(pages)
        
        source  = file_path.split("\\")[-1]
        
        for chunk in chunks:
            chunk["source"] = source

        return chunks