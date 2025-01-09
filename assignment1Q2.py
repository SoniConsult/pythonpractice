# mean=Sum of all observtion / total number of observation

def calculatingMean(*args):
    count=len(args)
    sum=0
    for i in args:
         sum+=i
    return f"{sum/count}"

def calculatingMedian(*args):
    median=0
    count=len(args)
    if count%2==0:
        first=count/2
        second=(count/2)+1
        median=(args[int(first)]+args[int(second)])/2
    else:
       median=args[ (count+1)/2]
    return median

from collections import Counter

def calculatingMode(*args):
    if len(args) == 0:
        return "No data provided"
    count = Counter(args) 
    max_count = max(count.values())
    mode = [key for key, value in count.items() if value == max_count]
    if len(mode) == 1:
        return mode[0]
    else:
        return mode

   
def main():
      print(calculatingMean(2,3,4,5,6))
      print(calculatingMedian(3,4,5,7,9,10))
      print(calculatingMode(3,3,3,4,5,7,7,7))


if __name__ == "__main__":
    main()
