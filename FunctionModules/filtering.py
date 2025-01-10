import fetchingDataFromFile as fi

content=fi.fetchingFile()

def filtering(word):
    if word in content:
        return True
    else :
        return False



print(filtering("Hello"))


def display():
    print (content)


display()