from app.utils.logger import log_event
from typing import TypedDict
from langgraph.graph import StateGraph, END

from app.rag.loader import load_documents
from app.agents.answer_agent import answer_agent
from app.agents.critic_agent import critic_agent


class GraphState(TypedDict):
    question: str
    context: str
    answer: str
    status: str
    retries: int

# STEP 1: Retrieve
def retrieve(state: GraphState):
    log_event("Retrieving context")
    print("🔍 Retrieving context...")
    docs = load_documents()
    context = "\n\n".join([doc["content"] for doc in docs])

    return {
        "question": state["question"],
        "context": context,
        "answer": "",
        "status": "",
        "retries": 0
    }


# STEP 2: Generate
def generate(state: GraphState):
    log_event("Generating answer")
    print("✍️ Generating answer...")
    answer = answer_agent(state["context"], state["question"])

    return {
        "question": state["question"],
        "context": state["context"],
        "answer": answer,
        "status": "",
        "retries": state["retries"]
    }


# STEP 3: Check
def check(state: GraphState):
    log_event("Checking answer")
    print("🧪 Checking answer...")

    # Stop after 2 retries
    if state["retries"] >= 2:
        print("⚠️ Max retries reached")
        return {
            "question": state["question"],
            "context": state["context"],
            "answer": state["answer"],
            "status": "good",  # force stop
            "retries": state["retries"]
        }

    result = critic_agent(state["answer"])

    if "GOOD" in str(result).upper():
        status = "good"
    else:
        status = "bad"

    return {
        "question": state["question"],
        "context": state["context"],
        "answer": state["answer"],
        "status": status,
        "retries": state["retries"] + 1
    }

def build_graph():
    builder = StateGraph(GraphState)

    builder.add_node("retrieve", retrieve)
    builder.add_node("generate", generate)
    builder.add_node("check", check)

    builder.set_entry_point("retrieve")

    builder.add_edge("retrieve", "generate")
    builder.add_edge("generate", "check")

    builder.add_conditional_edges(
        "check",
        lambda state: state["status"],
        {
            "good": END,
            "bad": "generate",
        },
    )

    return builder.compile()