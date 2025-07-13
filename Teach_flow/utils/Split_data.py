from langchain.schema import Document
def split_by_chunk_size(documents, chunk_size=1000):

    all_chunks = []

    doc_groups = {}
    for doc in documents:
        doc_id = doc.metadata.get("title") or doc.metadata.get("source_file") or "Unknown_Document"
        doc_groups.setdefault(doc_id, []).append(doc)

    # Process each grouped document
    for doc_id, docs in doc_groups.items():
        full_text = " ".join([doc.page_content for doc in docs])
        source_file = docs[0].metadata.get("source_file", doc_id)

        num_chunks = (len(full_text) + chunk_size - 1) // chunk_size

        for i in range(0, len(full_text), chunk_size):
            chunk_text = full_text[i:i + chunk_size]
            chunk_index = i // chunk_size

            chunk = Document(
                page_content=chunk_text,
                metadata={
                    "title": doc_id,
                    "source_file": source_file,
                    "chunk_index": chunk_index,
                    "total_chunks": num_chunks
                }
            )
            all_chunks.append(chunk)

        print(f"✅ Split document '{doc_id}' into {num_chunks} chunks")

    print(f"\n📄 Total chunks created: {len(all_chunks)}")
    return all_chunks
