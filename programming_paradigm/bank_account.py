class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initialize account with optional starting balance."""
        self.__account_balance = float(initial_balance)  # private attribute

    def deposit(self, amount):
        """Add amount to account balance. Return True on success."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw amount if funds are sufficient. Return True on success."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def get_balance(self):
        """Return current balance (float)."""
        return self.__account_balance

    def display_balance(self):
        """Print the current balance in the format: Current Balance: $[amount]"""
        bal = self.__account_balance
        # print as integer if it's a whole number, otherwise print the float
        if isinstance(bal, float) and bal.is_integer():
            bal_str = f"{int(bal)}"
        else:
            bal_str = f"{bal}"
        print(f"Current Balance: ${bal_str}")
