class BankAccount:
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def display_balance(self):
        print(f"Account owner: {self.owner}")
        print(f"Account balance: ₹{self.balance}")
        
account1 = BankAccount("Madhura", 5000)
account1.deposit(2000)
account1.withdraw(1000)
account1.display_balance()

