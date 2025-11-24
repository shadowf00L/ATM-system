def main():
    while True:
        print("\n---- ATM SYSTEM MENU ----")
        print("1. login")
        print("2. Deposit Money")
        print("3. Check Balance")
        print("4. Withdraw Money")
        print("5. Exit")

        choice= input("Enter your choice : ")
        if choice == '1':
            from login_page import login
            login() 
        
        elif choice == '2':
            from deposit_money import deposit_amount
            deposit_amount()

        elif choice == '3':
            from Balance_page import check_balance
            check_balance()

        elif choice == '4':
            from withdraw_money import withdraw_amount
            withdraw_amount()

        elif choice == '5':
            print("Thank you for using our ATM service!")
            break
        else:
            print("Invalid choice! Please select a valid option and try again.\n")


if __name__ == "__main__":
    main()