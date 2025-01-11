class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Error: Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Error: Insufficient funds. Available balance: ${self.balance}")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Account balance: ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.03):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest earned: ${interest:.2f}")
        return interest


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, transaction_limit=5):
        super().__init__(account_holder, balance)
        self.transaction_limit = transaction_limit
        self.transactions = 0

    def deposit(self, amount):
        if self.transactions >= self.transaction_limit:
            print("Error: Transaction limit reached.")
        else:
            super().deposit(amount)
            self.transactions += 1

    def withdraw(self, amount):
        if self.transactions >= self.transaction_limit:
            print("Error: Transaction limit reached.")
        else:
            super().withdraw(amount)
            self.transactions += 1

    def reset_transactions(self):
    
        self.transactions = 0
        print("Transaction count reset.")


class RewardsProgram:
    def __init__(self):
        self.rewards_points = 0

    def add_points(self, amount):
        points = amount 
        self.rewards_points += points
        print(f"Earned {points} points. Total points: {self.rewards_points}")

    def redeem_points(self, points):
        if points > self.rewards_points:
            print("Error: Not enough rewards points.")
        else:
            self.rewards_points -= points
            print(f"Redeemed {points} points. Remaining points: {self.rewards_points}")




def main():

    savings = SavingsAccount("Alice", 1000)
    savings.deposit(200)
    savings.calculate_interest()
    savings.check_balance()


    checking = CheckingAccount("Bob", 500, transaction_limit=3)
    checking.deposit(100)
    checking.withdraw(50)
    checking.withdraw(30)
    checking.deposit(200)
    checking.reset_transactions()
    checking.withdraw(20)
    rewards = RewardsProgram()
    rewards.add_points(150)
    rewards.add_points(70)
    rewards.redeem_points(15)
    rewards.redeem_points(50)


if __name__=="__main__":
    main()