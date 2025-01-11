class Transaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def __repr__(self):
        return f"Transaction(ID: {self.transaction_id}, Amount: {self.amount:.2f})"

    def __add__(self, other):
        if not isinstance(other, Transaction):
            raise TypeError("Can only add Transaction objects.")
        new_id = f"{self.transaction_id}+{other.transaction_id}"
        return Transaction(new_id, self.amount + other.amount)

    def __lt__(self, other):
        if not isinstance(other, Transaction):
            raise TypeError("Can only compare Transaction objects.")
        return self.amount < other.amount

    def __eq__(self, other):
        if not isinstance(other, Transaction):
            raise TypeError("Can only compare Transaction objects.")
        return self.amount == other.amount


def main():
    t1 = Transaction("T001", 150.75)
    t2 = Transaction("T002", 200.00)
    t3 = Transaction("T003", 150.75)
    print(t1)  
    print(t2)  
    t4 = t1 + t2
    print(t4) 
    print(t1 < t2)  
    print(t1 == t3) 
    print(t1 > t2)  
    try:
        t5 = t1 + 100 
    except TypeError as e:
        print(f"Error: {e}") 

if __name__=="__main__":
    main()