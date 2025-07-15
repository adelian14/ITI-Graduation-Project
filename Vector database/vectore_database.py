import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.http import VectorParams, Distance
from uuid import uuid4

load_dotenv()
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

def get_qdrant_client():
    
    client = QdrantClient(
        url=QDRANT_URL,
        api_key=QDRANT_API_KEY
    )
    return client

def create_collection(client, collection_name):
    client.recreate_collection(
    collection_name="machine_learning_chunks",
        vectors_config=VectorParams(
            size=768,
            distance=Distance.COSINE
        )
    )

def chunks_metadata(chunks):
    payloads = []
    ids = []

    for chunk in chunks:
        metadata = chunk["metadata"]
        payload = {
            "text": chunk["text"],
            "module": metadata.get("module_title"),
            "lesson": metadata.get("lesson_title"),
            "topic": metadata.get("topic_title"),
            "language": metadata.get("language"),
            "doc_title": metadata.get("document_title"),
            "module_number": metadata.get("module_number"),
            "lesson_number": metadata.get("lesson_number"),
            "topic_number": metadata.get("topic_number")
        }
        payloads.append(payload)
        ids.append(str(uuid4()))
    
    return payloads, ids

def upload_vectors(client, collection_name, chunks, vectors):
    payloads, ids = chunks_metadata(chunks)
    
    client.upload_collection(
        collection_name="machine_learning_chunks",
        vectors=vectors,
        payload=payloads,
        ids=ids
    )
    
    print(f"Uploaded {len(chunks)} chunks to collection '{collection_name}'")

def search_chunks(client, collection_name, query_vector, limit=5):
    results = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=limit
    )
    
    return results