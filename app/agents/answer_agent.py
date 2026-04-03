from app.utils.llm import get_llm_response
from app.memory.memory import get_history, save_message

def answer_agent(context, question):
    history = get_history()

    prompt = f"""
You are a helpful customer support assistant.

Conversation History:
{history}

Context:
{context}

Question:
{question}
"""

    response = get_llm_response(prompt)

    # Save conversation
    save_message("User", question)
    save_message("AI", response)

    return response