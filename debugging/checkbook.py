class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function Description:
        Deposits the specified amount into the account.

        Parameters:
        - amount: Amount to be deposited (float).

        Returns:
        - None.
        """
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function Description:
        Withdraws the specified amount from the account.

        Parameters:
        - amount: Amount to be withdrawn (float).

        Returns:
        - None.
        """
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function Description:
        Displays the current balance of the account.

        Parameters:
        - None.

        Returns:
        - None.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
