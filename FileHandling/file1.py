file=open("./FileHandling/sample.txt",'r')
file2=open("./FileHandling/sample.txt",'w')
file2.write("Friday")
content=file.read()

print(content)

file.close()
