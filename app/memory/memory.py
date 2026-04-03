chat_history = []

def save_message(role, message):
    chat_history.append({
        "role": role,
        "message": message
    })

def get_history():
    history_text = ""

    for msg in chat_history:
        history_text += f"{msg['role']}: {msg['message']}\n"

    return history_text