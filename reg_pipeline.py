from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import VECTORSTORE_PATH, EMBEDDING_MODEL


def build_vectorstore(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectordb = Chroma.from_documents(docs, embedding=embeddings, persist_directory=VECTORSTORE_PATH)
    vectordb.persist()
    return vectordb