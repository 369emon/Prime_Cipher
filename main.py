import auth
import messaging

BANNER = r"""
   ____       _                 ____ _     _       _           
  |  _ \ _ __(_)_   _____ _ __ / ___| |__ (_)_ __ | |__  _   _ 
  | |_) | '__| \ \ / / _ \ '__| |   | '_ \| | '_ \| '_ \| | | |
  |  __/| |  | |\ V /  __/ |  | |___| | | | | |_) | | | | |_| |
  |_|   |_|  |_| \_/ \___|_|   \____|_| |_|_| .__/|_| |_|\__, |
                                            |_|          |___/ 
---------------------------------------------------------------
        Secure Terminal Messaging - PrimeCipher
"""

COMMANDS = [
    "/login    - Log in to your account",
    "/send     - Send an encrypted message",
    "/read     - Read your messages",
    "/logout   - Log out of the session",
    "/help     - Show this help message"
]

def show_help():
    print("\nAvailable commands:")
    for cmd in COMMANDS:
        print("  " + cmd)
    print()

def main():
    print(BANNER)
    print("Welcome to PrimeCipher Terminal!\n")
    if auth.login():
        show_help()
        while True:
            cmd = input("primecipher> ").strip()
            if cmd == "/send":
                messaging.send_message()
            elif cmd == "/read":
                messaging.read_messages()
            elif cmd == "/logout":
                print("Logging out...")
                break
            elif cmd == "/help":
                show_help()
            elif cmd == "":
                continue
            else:
                print("Unknown command. Type /help for a list of commands.")

if __name__ == "__main__":
    main()