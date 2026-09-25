# RAG Document Assistant

🇪🇸 Español | 🇬🇧 [English](README.md)

Sistema de **Retrieval-Augmented Generation (RAG)** que permite subir documentos PDF y realizar preguntas sobre su contenido.

El sistema combina búsqueda semántica con un **Large Language Model (LLM)** local para recuperar fragmentos relevantes del documento y generar respuestas basadas en la información recuperada.

## Funcionalidades

- Carga y procesamiento de documentos PDF.
- Extracción de texto mediante PyMuPDF.
- División de documentos en fragmentos (*chunks*) con solapamiento.
- Generación de embeddings mediante Sentence Transformers.
- Búsqueda semántica mediante FAISS.
- Generación de respuestas utilizando Qwen 2.5 3B mediante Ollama.
- Referencias a las fuentes utilizadas para generar cada respuesta.
- API REST desarrollada con FastAPI.
- Interfaz web desarrollada con Streamlit.
- Tests automatizados mediante pytest.
