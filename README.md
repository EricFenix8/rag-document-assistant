# RAG Document Assistant

🇬🇧 English | 🇪🇸 [Español](README.es.md)

A Retrieval-Augmented Generation (RAG) system that allows users to upload PDF documents and ask questions about their content.

The system combines semantic search with a local Large Language Model (LLM) to retrieve relevant document passages and generate answers grounded in the uploaded document.

## Features

- PDF document upload and processing
- Text extraction with PyMuPDF
- Document chunking with configurable overlap
- Semantic embeddings using Sentence Transformers
- Vector similarity search with FAISS
- Local LLM inference using Ollama and Qwen 2.5 3B
- Source attribution with document name, page number and relevance score
- REST API built with FastAPI
- Interactive web interface built with Streamlit
- Automated tests with pytest

## Project Structure

The project is organized into several modules, each responsible for a specific part of the RAG pipeline.

The `app/` directory contains the core application logic. It includes modules for PDF loading, document processing, text chunking, embedding generation, vector storage, semantic retrieval, answer generation, and the FastAPI API.

The `tests/` directory contains automated tests for the main components of the system, including document processing, retrieval, the RAG pipeline, and API endpoints.

The `data/` directory contains the PDF documents used by the application.

The `frontend.py` file contains the Streamlit web interface, which allows users to upload documents and interact with the RAG system.

The `run_rag.py` script provides a simple way to run the RAG pipeline directly from Python without using the web interface.

The `requirements.txt` file contains the project's Python dependencies, while `pytest.ini` contains the pytest configuration.

## How It Works

1. **Document upload**  
   The user uploads a PDF through the Streamlit interface.

2. **Processing**  
   PyMuPDF extracts the text, which is then split into chunks while preserving page information.

3. **Embeddings**  
   Each chunk is converted into an embedding using `all-MiniLM-L6-v2`.

4. **Semantic search**  
   The user's question is also converted into an embedding, and FAISS retrieves the most relevant chunks.

5. **Answer generation**  
   The retrieved chunks are provided as context to Qwen 2.5 3B, running locally through Ollama.

6. **Sources**  
   The response includes the document, page number, and similarity score of the retrieved chunks.

## Installation

### Steps

```bash
git clone https://github.com/YOUR_USERNAME/rag-document-assistant.git
cd rag-document-assistant
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
ollama pull qwen2.5:3b
```

## Running the Application

The project uses a FastAPI backend and a Streamlit frontend.

Run them in two separate terminals:

```bash
uvicorn app.api:app --reload
```

```bash
streamlit run frontend.py
```

## Current Limitations

- The vector index is kept in memory.
- The latest processed document replaces the previous one.
- Vector indexes are not persisted.
- The embedding model is primarily optimized for English.
- The current chunking strategy uses a fixed word-based size.
- There is no formal evaluation system for retrieval or answer quality yet.

## Future Improvements

- Support for multiple documents.
- Persistent vector storage.
- Use of multilingual embeddings.
- Semantic chunking.
- Retrieval relevance thresholds.
- Result reranking.
- Conversation history.
- Streaming responses.
- Automated RAG evaluation.
- User authentication and document collections.
- Cloud deployment.