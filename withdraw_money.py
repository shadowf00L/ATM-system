# withdraw_amount.py

from account import account
from transaction_history import add_transaction


def withdraw_amount():
    print("""
---------------------
Money Withdrawal System
---------------------
""")

    try:
        amount = float(input("Enter the amount to withdraw: \u20B9"))
    except ValueError:
        print("Invalid input. Please enter a numeric amount.")
        return

    if amount <= 0:
        print("Invalid amount. Withdrawal must be greater than 0.")
        return

    balance = float(account.get('balance', 0.0))
    if amount > balance:
        print(f"Insufficient funds. Your current balance is: \u20B9{balance:.2f}")
        return

    account['balance'] = balance - amount
    # Record transaction
    try:
        add_transaction('withdrawal', amount, account['balance'], description='Withdrawal via withdraw_money')
    except Exception:
        pass

    print(f"\u20B9{amount:.2f} has been withdrawn from your account.")
    print(f"New balance: \u20B9{account['balance']:.2f}")
    print("Please collect your cash and receipt.\n")


if __name__ == "__main__":
    withdraw_amount()
