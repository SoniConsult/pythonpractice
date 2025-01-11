class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, item, quantity):
        try:
            if quantity <= 0:
                raise ValueError("Quantity to add must be greater than zero.")
            if item in self.stock:
                self.stock[item] += quantity
            else:
                self.stock[item] = quantity
            print(f"Added {quantity} of {item}. Current stock: {self.stock[item]}")
        except ValueError as e:
            print(f"Error: {e}")

    def remove_stock(self, item, quantity):
        
        try:
            if item not in self.stock:
                raise KeyError(f"Item '{item}' does not exist in the inventory.")
            if quantity <= 0:
                raise ValueError("Quantity to remove must be greater than zero.")
            if self.stock[item] < quantity:
                raise ValueError(f"Insufficient stock of {item}. Available: {self.stock[item]}")
            self.stock[item] -= quantity
            print(f"Removed {quantity} of {item}. Current stock: {self.stock[item]}")
            if self.stock[item] == 0:
                del self.stock[item]  # Remove item from inventory if stock becomes zero
        except (KeyError, ValueError) as e:
            print(f"Error: {e}")

    def query_item(self, item):
        if item in self.stock:
            print(f"{item}: {self.stock[item]} in stock.")
        else:
            print(f"{item} is not available in the inventory.")

    def check_insufficient_items(self, threshold):
       
        insufficient_items = {item: qty for item, qty in self.stock.items() if qty < threshold}
        if insufficient_items:
            print("Insufficient items (below threshold):")
            for item, qty in insufficient_items.items():
                print(f"- {item}: {qty}")
        else:
            print("No items are below the threshold.")

def main():
    inventory = Inventory()
    inventory.add_stock("Apples", 50)
    inventory.add_stock("Bananas", 20)
    inventory.query_item("Apples")
    inventory.query_item("Oranges")
    inventory.remove_stock("Apples", 30)
    inventory.remove_stock("Bananas", 25)  
    inventory.check_insufficient_items(15) 
    inventory.query_item("Apples")

if __name__=="__main__":
    main()



