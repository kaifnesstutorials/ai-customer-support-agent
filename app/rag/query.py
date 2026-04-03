from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from app.utils.llm import get_llm_response

def ask_question(query):
    embeddings = OpenAIEmbeddings()

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    docs = vectorstore.similarity_search(query, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a customer support assistant.

Answer the question using ONLY the context below.

Context:
{context}

Question:
{query}
"""

    response = get_llm_response(prompt)
    return response