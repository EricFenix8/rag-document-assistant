from app.document_processor import DocumentProcessor
from app.retriever import Retriever


class RAGPipeline:

    def __init__(self, chunk_size=100, overlap=20):
        self.document_processor = DocumentProcessor(
            chunk_size=chunk_size,
            overlap=overlap
        )
        self.retriever = Retriever()

    def add_pdf(self, file_path):
        chunks = self.document_processor.process_pdf(file_path)

        self.retriever.add_documents(chunks)

    def search(self, query, top_k=3):
        return self.retriever.search(
            query,
            top_k=top_k
        )