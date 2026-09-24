from app.document_processor import DocumentProcessor
from app.retriever import Retriever
from app.generator import Generator

class RAGPipeline:

    def __init__(self, chunk_size=100, overlap=20, model_name="qwen2.5:3b"):
        self.document_processor = DocumentProcessor(
            chunk_size=chunk_size,
            overlap=overlap
        )
        self.retriever = Retriever()
        self.generator = Generator(model_name=model_name)

    def add_pdf(self, file_path):
        chunks = self.document_processor.process_pdf(file_path)

        self.retriever.add_documents(chunks)

    def search(self, query, top_k=3):
        return self.retriever.search(
            query,
            top_k=top_k
        )
        
    def ask(self, question, top_k=3):
        results = self.search(
            question,
            top_k=top_k
        )

        context = "\n\n".join(
            result["text"]
            for result in results
        )

        answer = self.generator.generate(
            question,
            context
        )

        sources = [
            {
                "source": result["source"],
                "page": result["page"],
                "score": result["score"]
            }
            for result in results
        ]

        return {
            "answer": answer,
            "sources": sources
        }