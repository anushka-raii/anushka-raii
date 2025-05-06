# Custom Message Sender

def send_message(*, sender, recipient, message):
    return f"From {sender} to {recipient}: {message}"
print(send_message(sender="Alice", recipient="Bob", message="Hello there!"))


