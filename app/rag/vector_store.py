from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.rag.loader import load_documents

def create_vector_store():
    docs = load_documents()

    texts = [doc["content"] for doc in docs]

    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.from_texts(texts, embeddings)

    vectorstore.save_local("faiss_index")

    print("✅ Vector DB created successfully!")

if __name__ == "__main__":
    create_vector_store()