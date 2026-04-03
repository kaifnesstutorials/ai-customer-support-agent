import streamlit as st
from app.graph.workflow import build_graph

st.set_page_config(page_title="AI Support System", layout="centered")

st.title("🤖 AI Customer Support Assistant")

# Initialize graph
graph = build_graph()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input (no need to erase anything)
user_input = st.chat_input("Ask your question...")

if user_input:

    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    result = graph.invoke({
        "question": user_input,
        "context": "",
        "answer": "",
        "status": "",
        "retries": 0
    })

    ai_response = result["answer"]

    # Show AI message
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.markdown(ai_response)