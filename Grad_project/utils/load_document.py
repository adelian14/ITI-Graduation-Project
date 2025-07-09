import os
from langchain.document_loaders import (
    PyMuPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredPowerPointLoader,
)

def load_documents(directory_path):
    """Load all PDF, TXT, DOCX, and PPTX documents from a directory"""
    documents = []
    titles = []

    for filename in os.listdir(directory_path):
        path = os.path.join(directory_path, filename)
        ext = os.path.splitext(filename)[1].lower()

        # Select appropriate loader
        if ext == ".pdf":
            loader = PyMuPDFLoader(path)
        elif ext == ".txt":
            loader = TextLoader(path, encoding="utf-8")
        elif ext == ".docx":
            loader = UnstructuredWordDocumentLoader(path)
        elif ext == ".pptx":
            loader = UnstructuredPowerPointLoader(path)
        else:
            print(f"Skipping unsupported file: {filename}")
            continue

        try:
            # Load and enrich documents
            docs = loader.load()
            title = os.path.splitext(filename)[0]
            titles.append(title)

            for doc in docs:
                doc.metadata["title"] = title
                doc.metadata["source_file"] = filename

            documents.extend(docs)
            print(f"Loaded document: {filename}")
        except Exception as e:
            print(f"Failed to load {filename}: {e}")

    print(f"\n✅ Total documents loaded: {len(documents)}")
    return documents, titles
