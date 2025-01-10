import csv

file = open('./FileHandling/data.csv')
print(file)
csvreader = csv.reader(file)

print(csvreader)
type(file)