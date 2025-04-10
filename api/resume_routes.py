from fastapi import APIRouter, UploadFile
from resume_extractor import extract_resume_text
from rag_pipeline import build_vectorstore
import os

router = APIRouter()

@router.post("/upload")
def upload_resume(file: UploadFile):
    path = f"data/resumes/{file.filename}"
    with open(path, "wb") as f:
        f.write(file.file.read())
    return {"message": "Resume uploaded.", "path": path}

@router.post("/extract")
def extract_resume(file_path: str):
    text = extract_resume_text(file_path)
    vectordb = build_vectorstore(text)
    return {"message": "Resume processed.", "chunks": len(vectordb.get())}