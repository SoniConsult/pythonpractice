import csv
from collections import defaultdict


total_sales = 0
product_sales = defaultdict(int)
transaction_count = 0 


with open('./FileHandling/data.csv', 'r') as file:
    reader = csv.DictReader(file)  
    for row in reader:
        product = row['Product']
        quantity = int(row['Quantity'])
        price = float(row['Price'])
        

        total_sales += quantity * price
        
       
        product_sales[product] += quantity
        
      
        transaction_count += 1


average_sales = total_sales / transaction_count if transaction_count > 0 else 0


top_selling_product = max(product_sales, key=product_sales.get)
top_quantity = product_sales[top_selling_product]


print(f"Total Sales: ${total_sales}")
print(f"Average Sales: ${average_sales}")
print(f"Top-Selling Product: {top_selling_product} (Quantity Sold: {top_quantity})")
