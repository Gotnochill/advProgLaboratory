# 8. Banking system (deposit, withdraw)
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

if __name__ == "__main__":
    acc = BankAccount("Alice", 100)
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(150)