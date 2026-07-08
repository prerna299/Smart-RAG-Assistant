from langchain_community.vectorstores import FAISS
from utils.embeddings import get_embedding_model

INDEX_PATH = "faiss_index"


def create_vector_store(chunks):
    embeddings = get_embedding_model()

    vector_store = FAISS.from_documents(chunks, embeddings)

    vector_store.save_local(INDEX_PATH)

    return vector_store


def load_vector_store():
    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store