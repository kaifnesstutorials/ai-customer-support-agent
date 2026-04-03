import datetime

def log_event(message):
    with open("logs/system.log", "a") as f:
        time = datetime.datetime.now()
        f.write(f"[{time}] {message}\n")