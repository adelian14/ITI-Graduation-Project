from sentence_transformers import SentenceTransformer

def load_embedding_model():
    """
    Load a pre-trained embedding model from Sentence Transformers.

    Args:
        model_name (str): The name of the model to load. Default is 'BAAI/bge-base-en-v1.5'.

    Returns:
        SentenceTransformer: The loaded embedding model.
    """
    model_name='BAAI/bge-base-en-v1.5'

    return SentenceTransformer(model_name)

def data_embedding(chunks):

    emmpding_model = load_embedding_model()

    texts = [chunk["text"] for chunk in chunks]
    vectors = emmpding_model.encode(texts).tolist()

    return vectors
