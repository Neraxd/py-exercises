import random
import string

class BankAccount:
    total_accounts = 0

    def __init__(self, owner, balance):
        self.__balance = balance
        # generate a 7-digit account number as a string
        self.__account_number = ''.join(random.choices(string.digits, k=7))
        self._owner = owner
        BankAccount.total_accounts += 1

    def deposit(self, amount):
        self.__balance += amount
        print(f"Successful deposit!\nNew balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Successful withdraw!\nNew balance: {self.__balance}")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        print("Cannot change balance directly!")

    @staticmethod
    def bank_rules():
        print("One and only rule: cannot access the balance directly")


# Example usage
acc1 = BankAccount("Alice", 500)
acc2 = BankAccount("Bob", 1000)

acc1.deposit(200)
acc2.withdraw(300)

print(acc1.balance)
print(BankAccount.total_accounts)
BankAccount.bank_rules()

