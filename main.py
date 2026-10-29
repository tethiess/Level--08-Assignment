from bank_functions import BankAccount


def main():
    customer_name = input("Please enter your name: ")
    account = BankAccount(account_holder=customer_name)
    print(f"Your account has been created. Your account number is {account.account_number}.")
    print(f"Starting balance: ${account.balance:.2f}")
    account.account_actions()


if __name__ == "__main__":
    main()
