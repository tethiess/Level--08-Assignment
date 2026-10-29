import random


class BankAccount:
    def __init__(self, account_holder, account_number=None, balance=0.00):
        self.account_holder = account_holder
        self.account_number = account_number if account_number is not None else random.randint(10000, 99999)
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if amount > self.balance:
            raise ValueError("Insufficient funds. You cannot withdraw more than your current balance.")
        self.balance -= amount
        return self.balance

    def view_account_info(self):
        return (
            f"Name: {self.account_holder}\n"
            f"Account #: {self.account_number}\n"
            f"Balance: ${self.balance:.2f}"
        )

    def account_actions(self):
        print("Welcome to the Bank of Tyler!")
        print(f"Welcome, {self.account_holder}.")

        while True:
            print("\nPlease choose an option:")
            print("1. Make a deposit")
            print("2. Make a withdrawal")
            print("3. View account information")
            print("4. Quit")

            user_select = input("Enter your choice: ")

            try:
                choice = int(user_select)
            except ValueError:
                print("Invalid selection. Please enter a valid menu option.")
                continue

            if choice == 1:
                deposit_amount = input("How much would you like to deposit? ")
                try:
                    amount = float(deposit_amount)
                    self.deposit(amount)
                    print(f"Deposit successful. New balance: ${self.balance:.2f}")
                except ValueError as error:
                    print(error)

            elif choice == 2:
                withdrawal_amount = input("How much would you like to withdraw? ")
                try:
                    amount = float(withdrawal_amount)
                    self.withdraw(amount)
                    print(f"Withdrawal successful. New balance: ${self.balance:.2f}")
                except ValueError as error:
                    print(error)

            elif choice == 3:
                print(self.view_account_info())

            elif choice == 4:
                print("Thank you for your business!")
                break

            else:
                print("Invalid selection. Please choose a valid option.")


