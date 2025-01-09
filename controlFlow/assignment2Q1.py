import math
def isPrime(num):
    prime_flag = 0
    if num==1:
       print("False")
    if(num > 1):
      for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            prime_flag = 1
            break
    if (prime_flag == 0):
        print("True")
    else:
        print("False")
        

def isComposite(num):
      if (num <= 1):
        return False
      if (num <= 3):
        return False
      if (num % 2 == 0 or num% 3 == 0):
        return True
      i = 5
      while(i * i <= num):
         
        if (num% i == 0 or num % (i + 2) == 0):
            return True
        i = i + 6
        
      return False

   
def main():
   isPrime(7)
   print(isComposite(12))

if __name__ == "__main__":
    main()