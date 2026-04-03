import os

def load_documents():
    base_path = "knowledge_base"
    documents = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                documents.append({
                    "content": content,
                    "source": file_path
                })

    return documents