import os

LLAMA_MODEL_PATH = os.getenv("LLAMA_MODEL_PATH", "models/llama/model.bin")
LLAMA_ADAPTER_PATH = os.getenv("LLAMA_ADAPTER_PATH", "models/llama/adapter")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTORSTORE_PATH = "models/embeddings"