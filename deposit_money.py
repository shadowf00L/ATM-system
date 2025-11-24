#deposit_moneny.py

from account import account
from transaction_history import add_transaction

def deposit_amount():
    print("""
Money Deposit System
""")
    print("Welcome to ATM!\n")

    try:
        amount = float(input("Enter the amount to be deposited: \u20B9"))
    except ValueError:
        print("Invalid input. Please enter a numeric amount.")
        return

    if amount <= 0:
        print("Invalid Amount! Deposit should be greater than 0" )
        return

    # Updating in-memory account balance:
    account['balance'] = float(account.get('balance', 0.0)) + amount

    # Record transaction
    try:
        add_transaction('deposit', amount, account['balance'], description='Deposit via deposit_money')
    except Exception:
        pass

    print(f"\u20B9{amount:.2f} has been successfully deposited to your account.")
    print(f"New balance: \u20B9{account['balance']:.2f}")
    print("Please collect your receipt.\n")
    print("Thank you for using our ATM service!")


if __name__ == "__main__":
    deposit_amount()