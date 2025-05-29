import auth
import messaging

BANNER = r"""
   
__________        .__                 _________ .__       .__                  
\______   \_______|__| _____   ____   \_   ___ \|__|_____ |  |__   ___________ 
 |     ___/\_  __ \  |/     \_/ __ \  /    \  \/|  \____ \|  |  \_/ __ \_  __ \
 |    |     |  | \/  |  Y Y  \  ___/  \     \___|  |  |_> >   Y  \  ___/|  | \/
 |____|     |__|  |__|__|_|  /\___  >  \______  /__|   __/|___|  /\___  >__|   
                           \/     \/          \/   |__|        \/     \/       
    
  
---------------------------------------------------------------
        Secure Terminal Messaging - PrimeCipher
"""

COMMANDS = [
    "/l    - Log in to your account",
    "/s    - Send an encrypted message",
    "/r    - Read your messages",
    "/lo   - Log out of the session",
    "/h     - Show this help message"
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
            if cmd == "/s":
                messaging.send_message()
            elif cmd == "/r":
                messaging.read_messages()
            elif cmd == "/lo":
                print("Logging out...")
                break
            elif cmd == "/h":
                show_help()
            elif cmd == "":
                continue
            else:
                print("Unknown command. Type /help for a list of commands.")

if __name__ == "__main__":
    main()