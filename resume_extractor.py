import os
from langchain.document_loaders import PyPDFLoader
from utils import clean_text


def extract_resume_text(pdf_path: str) -> str:
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    full_text = "\n".join([page.page_content for page in pages])
    return clean_text(full_text)
