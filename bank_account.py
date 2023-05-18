# Assignment: Bank Account

#! The BankAccount class should have a balance. When a new BankAccount instance is created,
# if an amount is given, the balance of the account should initially be set to that amount; otherwise,
# the balance should start at $0. The account should also have an interest rate in decimal format.
# For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation.
# (Hint: when using default values in parameters, the order of parameters matters!)

class BankAccount:
    accounts = []

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    # deposit(self, amount) - increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        return self

    # withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
        # if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 Overdfraft Fee")
            self.balance -= 5
        return self

    # display_account_info(self) - print to the console: eg. "Balance: $100"
    def display_account_info(self):
            print(f"Balance: {self.balance}")
            return self


    # yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)
    def yield_interest(self):
            if self.balance > 0:
                self.balance += (self.balance * self.int_rate)
            return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = BankAccount(.05, 3500)
checking = BankAccount(.02, 6548)

savings.deposit(100).deposit(75).deposit(200).withdraw(225).yield_interest().display_account_info()
checking.deposit(520).deposit(100).deposit(250).withdraw(300).yield_interest().display_account_info()