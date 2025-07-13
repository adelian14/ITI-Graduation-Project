from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def create_vector_store(chunks):
    """
    Create a vector store from document chunks
    """
    print("Creating vector store...")
    # Using HuggingFace embeddings (open-source alternative)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    # Create the vector store
    vector_store = FAISS.from_documents(chunks, embeddings)
    print("Vector store created successfully")
    return vector_store