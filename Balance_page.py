# Balance_page.py
# Simple balance check that reads the shared `account` object

from account import account


def check_balance():
    balance = float(account.get('balance', 0.0))
    print(f"\nYour current balance is: \u20B9{balance:.2f}\n")


def main():
    print("*** ATM SYSTEM ***")
    print("1. Check Balance")
    print("2. Exit")

    try:
        choice = int(input("Provide your option: "))
    except ValueError:
        print("\nInvalid choice! Please enter 1 or 2.")
        return

    if choice == 1:
        check_balance()
    elif choice == 2:
        print("\nThank you for using our ATM service!")
    else:
        print("\nInvalid choice!")


if __name__ == "__main__":
    main()
