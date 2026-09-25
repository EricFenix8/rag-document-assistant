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

## Estructura del proyecto

El proyecto está organizado en varios módulos, cada uno responsable de una parte específica del pipeline RAG.

El directorio `app/` contiene la lógica principal de la aplicación. Incluye los módulos encargados de cargar los PDFs, procesar los documentos, dividir el texto en fragmentos, generar embeddings, almacenar los vectores, realizar la recuperación semántica, generar las respuestas y proporcionar la API de FastAPI.

El directorio `tests/` contiene los tests automatizados de los principales componentes del sistema, incluyendo el procesamiento de documentos, la recuperación, el pipeline RAG y los endpoints de la API.

El directorio `data/` contiene los documentos PDF utilizados por la aplicación.

El archivo `frontend.py` contiene la interfaz web desarrollada con Streamlit, que permite a los usuarios subir documentos e interactuar con el sistema RAG.

El script `run_rag.py` permite ejecutar el pipeline RAG directamente desde Python sin utilizar la interfaz web.

El archivo `requirements.txt` contiene las dependencias Python del proyecto, mientras que `pytest.ini` contiene la configuración utilizada por pytest.

## Cómo funciona
1. **Subida del documento**  
   El usuario sube un PDF desde la interfaz de Streamlit.

2. **Procesamiento**  
   PyMuPDF extrae el texto y el sistema lo divide en fragmentos (*chunks*) manteniendo la información de cada página.

3. **Embeddings**  
   Cada fragmento se transforma en un embedding utilizando `all-MiniLM-L6-v2`.

4. **Búsqueda semántica**  
   La pregunta del usuario también se transforma en un embedding y FAISS recupera los fragmentos más relevantes.

5. **Generación de respuesta**  
   Los fragmentos recuperados se utilizan como contexto para Qwen 2.5 3B, ejecutado localmente mediante Ollama.

6. **Fuentes**  
   La respuesta incluye el documento, la página y el score de similitud de los fragmentos recuperados.


## Instalación
### Pasos

```bash
git clone https://github.com/YOUR_USERNAME/rag-document-assistant.git
cd rag-document-assistant
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
ollama pull qwen2.5:3b
```
## Ejecución
El proyecto usa un backend con FastAPI y un frontend con Streamlit

Ejecutar en dos terminales distintas:

```bash
uvicorn app.api:app --reload
```

```bash
streamlit run frontend.py
```

## Limitaciones actuales

- El índice vectorial se mantiene en memoria.
- El último documento procesado sustituye al anterior.
- Los índices vectoriales no se persisten.
- El modelo de embeddings está principalmente optimizado para inglés.
- El chunking utiliza actualmente un tamaño fijo basado en palabras.
- No existe todavía un sistema formal de evaluación de la calidad del retrieval o de las respuestas.

## Mejoras futuras

- Soporte para múltiples documentos.
- Persistencia del índice vectorial.
- Uso de embeddings multilingües.
- Chunking semántico.
- Umbrales de relevancia.
- Reranking de resultados.
- Historial de conversación.
- Streaming de respuestas.
- Evaluación automática del sistema RAG.
- Autenticación y colecciones de documentos por usuario.
- Despliegue en la nube.