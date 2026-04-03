# 🤖 AI Customer Support Agent (Multi-Agent, RAG, LangGraph)

A production-grade AI customer support system built using **LangGraph, OpenAI, and RAG architecture**.

This system simulates a real-world customer support assistant with **multi-agent orchestration, memory, retry logic, and monitoring**.

---

## 🚀 Features

* 🧠 **Multi-Agent System (LangGraph)**

  * Retriever Agent
  * Answer Agent
  * Critic Agent (self-evaluation)

* 📚 **RAG (Retrieval-Augmented Generation)**

  * Uses custom knowledge base (FAQs, policies, tickets)
  * FAISS vector database for semantic search

* 🔁 **Retry Mechanism**

  * Automatic answer correction using critic agent
  * Prevents low-quality responses

* 💬 **Conversational Memory**

  * Maintains chat history across queries

* 📊 **Logging & Monitoring**

  * Tracks system activity (retrieval, generation, validation)

* 🌐 **Interactive UI**

  * Built with Streamlit (chat-style interface)

---

## 🧱 Architecture

User Query
→ Retrieve Context (FAISS + embeddings)
→ Generate Answer (LLM)
→ Critic Agent (quality check)
→ Retry if needed
→ Final Response

---

## 🛠️ Tech Stack

* **LLM:** OpenAI API (GPT-4.1-mini)
* **Orchestration:** LangGraph
* **RAG:** LangChain + FAISS
* **Backend:** Python
* **UI:** Streamlit
* **Monitoring:** Custom logging system

---

## 📁 Project Structure

```
ai-customer-support-system/
│
├── app/
│   ├── agents/
│   ├── graph/
│   ├── rag/
│   ├── utils/
│   ├── memory/
│
├── knowledge_base/
├── logs/
├── app_ui.py
├── main.py
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```
git clone <your-repo-link>
cd ai-customer-support-agent
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add OpenAI API Key

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

### Run backend (CLI)

```
python main.py
```

### Run UI

```
streamlit run app_ui.py
```

---

## 💡 Example Use Cases

* Customer support automation
* FAQ answering systems
* AI helpdesk assistants
* E-commerce support bots

---

## 🔥 Key Highlights

* Built **multi-agent AI system using LangGraph**
* Implemented **RAG pipeline with FAISS**
* Designed **self-correcting AI with retry loop**
* Added **memory + logging for production readiness**
* Developed **interactive UI for real-world usage**

---

## 📌 Future Improvements

* Add FastAPI backend
* Deploy on cloud (AWS/GCP)
* Add real-time database
* Integrate analytics dashboard

---

## 👨‍💻 Author
Mohd Kaif Shaikh
,AI and DS graduate

---

