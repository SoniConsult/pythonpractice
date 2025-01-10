

balance=0
def initialize_account():
    name=input("Enter account holder's name")
    password=input("Enter pasword")
    accountNumber=input("Enter account Number")
    accountDetails={
        "Name": name,
        "Password":password,
        "Account Number":accountNumber
    }
    return accountDetails

def currentBalance():
    print(balance)
def displayMenu():
    global balance
    choice=input("Enter 1 , if you want to  deposit money, Enter 2, if you want to withdraw money")
    
    if(choice=="1"):
       deposit=float(input("Enter the money for deposit"))
       balance=balance+deposit
    elif choice=="2":
        withdraw=float(input("Enter the withdraw amount"))
        if(balance==0):
            print("Balance is not available")
        elif(withdraw>balance):
            print("Not available balance")
        else:
            balance-=withdraw
    else:
        print("Enter a valid choice")

def main():
    initialize_account()
    currentBalance()
    displayMenu()
    currentBalance()


if __name__=="__main__":
    main()
