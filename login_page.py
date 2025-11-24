# login_page.py
# ATM system (login helper)

from account import account

def login(max_attempts: int = 3) -> bool:
    
    for attempt in range(1, max_attempts + 1):
        pin = input("Enter your ATM pin: ")
        if pin == account.get("pin"):
            print("Authentication successful!\n")
            return True
        else:
            remaining = max_attempts - attempt
            if remaining > 0:
                print(f"Authentication failed. {remaining} attempt(s) remaining.\n")
            else:
                print("Authentication failed. No remaining attempts.\n")
    print("Your card has been temporarily blocked due to multiple failed attempts!")
    return False


if  __name__ == "__main__":
    login()