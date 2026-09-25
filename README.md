# RAG Document Assistant

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
