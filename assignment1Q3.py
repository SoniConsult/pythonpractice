def calculatingEMI(principal,rate, n):
    emi=(principal*rate*(1+rate)**n)/((1+rate)**n -1)
    return f"{emi}"

def main():
 print(calculatingEMI(100000,12,2))
 

if __name__ == "__main__":
    main()
