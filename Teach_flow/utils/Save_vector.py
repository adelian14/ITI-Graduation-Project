from utils.load_document import load_documents
from utils.Split_data import split_by_chunk_size
from utils.Vector_store import create_vector_store
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
#course_name="classical machine learning"
#saved_name=course_name+"vector"
vector_database={}
def get_vector_store(folder_path,found,course_name,saved_name):
    if found==False:
        documents, candidate_names = load_documents(folder_path)
        chunks=split_by_chunk_size(documents)
        vector_store = create_vector_store(chunks)
        vector_store.save_local(saved_name)
        vector_database[course_name]=saved_name
    else:
        vector_store = FAISS.load_local(saved_name, HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2"),allow_dangerous_deserialization=True)
    return vector_store
