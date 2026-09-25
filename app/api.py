from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from app.rag_pipeline import RAGPipeline


app = FastAPI(
    title="RAG Document Assistant",
    description="API for asking questions about PDF documents using RAG.",
    version="1.0.0"
)


pipeline = RAGPipeline(
    chunk_size=100,
    overlap=20
)


class QuestionRequest(BaseModel):
    question: str
    top_k: int = 3


@app.get("/")
def root():
    return {
        "message": "RAG Document Assistant API"
    }


@app.post("/documents")
async def upload_document(
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported."
        )

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    pipeline.add_pdf(file_path)

    return {
        "message": "Document processed successfully.",
        "filename": file.filename
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    result = pipeline.ask(
        request.question,
        top_k=request.top_k
    )

    return result