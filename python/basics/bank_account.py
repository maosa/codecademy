"""

In this project, we’ll create a Python class that can be used to create and manipulate a personal bank account.

The bank account class you’ll create should have methods for each of the following:

1) Accepting deposits
2) Allowing withdrawals
3) Showing the balance
4) Showing the details of the account

"""

class BankAccount(object):

    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "\nAccount holder: %s\nAvailable balance: %.2f\n" % (self.name, self.balance)

    def show_balance(self):
        print("\nAvailable balance: %.2f\n" % self.balance)

    def deposit(self, amount):
        if amount <= 0:
            print("\nInvalid amount entered!\n")
            return
        else:
            print("\nAmount deposited: %.2f\n" % amount)
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        if amount > self.balance:
            print("\nNot enough funds available!\n")
        else:
            print("\nAmount withdrawed: %.2f\n" % amount)
            self.balance -= amount
            self.show_balance()

##### Check code
my_account = BankAccount("Andreas")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
