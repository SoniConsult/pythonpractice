class Library:
    def __init__(self):
        self.books = {}  
        self.borrowed_books = {}

    def add_book(self, book_name, quantity):
        if book_name in self.books:
            self.books[book_name] += quantity
        else:
            self.books[book_name] = quantity
        print(f"{quantity} copies of '{book_name}' added to the library.")

    def view_books(self):
        print("\nAvailable Books:")
        if not self.books:
            print("No books available in the library.")
        else:
            for book, qty in self.books.items():
                print(f"{book} - {qty} copies")
        print()

    def borrow_book(self, user, book_name):
        if book_name not in self.books or self.books[book_name] == 0:
            print(f"Sorry, '{book_name}' is not available right now.")
        else:
            self.books[book_name] -= 1
            if user in self.borrowed_books:
                self.borrowed_books[user].append(book_name)
            else:
                self.borrowed_books[user] = [book_name]
            print(f"'{book_name}' has been borrowed by {user}.")

    def return_book(self, user, book_name):
        if user not in self.borrowed_books or book_name not in self.borrowed_books[user]:
            print(f"{user} did not borrow '{book_name}'.")
        else:
            self.borrowed_books[user].remove(book_name)
            if not self.borrowed_books[user]:
                del self.borrowed_books[user]
            self.books[book_name] = self.books.get(book_name, 0) + 1
            print(f"'{book_name}' has been returned by {user}.")

    def view_borrowed_books(self):
        print("\nBorrowed Books:")
        if not self.borrowed_books:
            print("No books are currently borrowed.")
        else:
            for user, books in self.borrowed_books.items():
                print(f"{user}: {', '.join(books)}")
        print()


# Main Program
library = Library()

while True:
    print("Library Management System")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Borrowed Books")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        book_name = input("Enter the book name: ")
        quantity = int(input("Enter the quantity: "))
        library.add_book(book_name, quantity)

    elif choice == '2':
        library.view_books()

    elif choice == '3':
        user = input("Enter your name: ")
        book_name = input("Enter the book name to borrow: ")
        library.borrow_book(user, book_name)

    elif choice == '4':
        user = input("Enter your name: ")
        book_name = input("Enter the book name to return: ")
        library.return_book(user, book_name)

    elif choice == '5':
        library.view_borrowed_books()

    elif choice == '6':
        print("Exiting Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
