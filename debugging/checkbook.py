#!/usr/bin/python3

class Checkbook:
    """
    A simple checkbook class to manage deposits, withdrawals, and balance tracking.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds a specified amount to the balance.

        Parameters:
        amount (float): The amount to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts a specified amount from the balance if sufficient funds exist.

        Parameters:
        amount (float): The amount to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    The main function that interacts with the user to perform checkbook operations.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
