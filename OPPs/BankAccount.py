class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
    
    def bank_account_check(self):
        try:
            if self.balance < 0:
                raise ValueError("Balance cannot be negative.")
            print(f"Account balance: ${self.balance}")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    account = BankAccount("Alice", 100)
    account.deposit(50)        
    account.deposit(-10)       
    account.withdraw(30)      
    account.withdraw(200)     
    account.bank_account_check() 

if __name__ == "__main__":
    main()


