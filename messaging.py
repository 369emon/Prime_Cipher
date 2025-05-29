messages = []

def send_message():
    msg = input("Enter message: ")
    # TODO: Encrypt and store message
    messages.append(msg)
    print("Message sent (encrypted).")

def read_messages():
    # TODO: Decrypt and display messages
    if not messages:
        print("No new messages.")
    else:
        print("Your messages:")
        for i, msg in enumerate(messages, 1):
            print(f"{i}: {msg}")
        messages.clear()  # Simulate self-destruct after reading