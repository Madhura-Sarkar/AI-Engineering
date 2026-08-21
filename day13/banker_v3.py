class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
    def display_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: ₹{self.balance}")
    
account1 = BankAccount("Madhura", 5000)

try:
    account1.deposit(-500)
except ValueError as error:
    print("Error:", error)
    
try:
    account1.withdraw(10000)
except ValueError as error:
    print("Error:", error)
    
account1.display_balance()
