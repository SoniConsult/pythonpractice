# creating an empty lists
books=[]

def addBooks(*args):
    for book in args:
        books.append(f"{book}")


def removeBooks(*args,index=len(books)):
    if len(books)==0:
        print("No books are available")
    
    if index!=0 and index<len(books):
        books.pop(index)
    for book in args:
        books.remove(f"{book}")
    
   

def searchBooks(book):
    for i in books:
        if i==book:
            return True

    return False


def ListingAllAvialableBooks():
    for book in books:
        print(book)

   

def main():
     while True:
        print("\nMenu:")
        print("1. Add Books")
        print("2. Remove Books")
        print("3. Search Books")
        print("4. List All Available Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            books_to_add = input("Enter the books to add (comma-separated): ").split(',')
            addBooks(*[book.strip() for book in books_to_add])
            print("Books added successfully!")
        
        elif choice == "2":
            books_to_remove = input("Enter the books to remove (comma-separated) or type 'index:<number>' to remove by index: ")
            if books_to_remove.startswith("index:"):
                try:
                    index = int(books_to_remove.split(":")[1].strip())
                    removeBooks(index=index)
                    print("Book removed by index successfully!")
                except (ValueError, IndexError):
                    print("Invalid index.")
            else:
                removeBooks(*[book.strip() for book in books_to_remove.split(',')])
                print("Books removed successfully!")
        
        elif choice == "3":
            book_to_search = input("Enter the name of the book to search: ").strip()
            found = searchBooks(book_to_search)
            print(f"Book '{book_to_search}' is {'available' if found else 'not available'}.")
        
        elif choice == "4":
            print("Listing all available books:")
            ListingAllAvialableBooks()
        
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()