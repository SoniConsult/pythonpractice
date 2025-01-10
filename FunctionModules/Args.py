def product(*args):
    product = 1
    for num in args:
        product *= num
    return product

def getInput():
    numbers = []
    while True:
        try:
            input1= input("Enter a number (or type 'done' to finish): ")
            
            if input1.lower() == 'done':
                break
            number = float(input1)
            numbers.append(number)
        
        except ValueError:
            print("Invalid input! Please enter a valid number or 'done'.")
    
    return numbers

numbers = getInput()

product = product(numbers)
print("The product of the numbers is:", product)
