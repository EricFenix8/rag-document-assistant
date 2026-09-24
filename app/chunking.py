class TextChunker:

    def __init__(self, chunk_size=100, overlap=20):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, text):
        words = text.split()

        chunks = []

        start = 0

        while start < len(words):
            end = start + self.chunk_size

            chunk = " ".join(words[start:end])
            chunks.append(chunk)

            start += self.chunk_size - self.overlap

        return chunks
    
    #Divide el texto de cada pagina en chunks y luego se recorren añadiendoles el num de pag
    def split_pages(self,pages):
        chunks = []
        for page in pages:
            page_chunks = self.split(page["text"])
            
            for chunk in page_chunks:
                chunks.append({
                    "text": chunk,
                    "page": page["page"]
                })
        return chunks