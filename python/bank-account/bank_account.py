class BankAccount:
    def __init__(self):
        self.IS_OPEN = None
        self.CURRENT_BALANCE = 0
        pass

    def get_balance(self):
        if self.IS_OPEN:
            return self.CURRENT_BALANCE
        else:
            raise ValueError("Account is Closed.")
        pass

    def open(self):
        if self.IS_OPEN == None:
            self.IS_OPEN = True
        elif self.IS_OPEN == True:
            raise ValueError("Already Opened.")
        elif self.IS_OPEN == False:
            self.IS_OPEN = True
            self.CURRENT_BALANCE = 0
        pass

    def deposit(self, amount):
        if self.IS_OPEN == False:
            raise ValueError("Account is Closed.")
        elif amount > 0:
            self.CURRENT_BALANCE += amount
        else:
            raise ValueError("amount is must be positive value.")
        pass

    def withdraw(self, amount):
        if self.IS_OPEN == False:
            raise ValueError("Account is Closed.")
        elif amount < 0:
            raise ValueError("amount must be positive value.")
        elif self.CURRENT_BALANCE - amount < 0:
            raise ValueError("You cannot withdraw money.")
        else:
            self.CURRENT_BALANCE -= amount
        pass

    def close(self):
        if self.IS_OPEN == None:
            raise ValueError("You have to open an account first.")
        elif self.IS_OPEN == True:
            self.IS_OPEN = False
        elif self.IS_OPEN == False:
            raise ValueError("Account is already closed.")
        pass
