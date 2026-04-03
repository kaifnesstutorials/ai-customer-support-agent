print("🚀 Starting program...")

from app.graph.workflow import build_graph

if __name__ == "__main__":
    graph = build_graph()

    # -------- First Question --------
    question1 = "What is your refund policy?"

    result1 = graph.invoke({
        "question": question1,
        "context": "",
        "answer": "",
        "status": "",
        "retries": 0
    })

    print("\n🧠 Answer 1:\n")
    print(result1["answer"])

    # -------- Second Question (tests memory) --------
    question2 = "How long does it take?"

    result2 = graph.invoke({
        "question": question2,
        "context": "",
        "answer": "",
        "status": "",
        "retries": 0
    })

    print("\n🧠 Answer 2 (with memory):\n")
    print(result2["answer"])