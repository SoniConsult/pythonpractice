

def fetchingFile():
    file = open("./FunctionModules/sample.txt", "r")
    content = file.read()
    file.close()
    return content
    