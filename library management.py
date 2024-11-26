class Library:
    def __init__(self, books):
        self.books = books

    def display_available_books(self):
        print("Available books in the library:")
        for book in self.books:
            print(book)

    def lend_book(self, requested_book):
        if requested_book in self.books:
            print("You have borrowed the book:", requested_book)
            self.books.remove(requested_book)
        else:
            print("Sorry, the book is not available.")

    def add_book(self, returned_book):
        self.books.append(returned_book)
        print("You have returned the book:", returned_book)


def main():
    books = ["Python Programming", "Java Programming", "JavaScript Basics", "C++ Programming"]
    library = Library(books)
    while True:
        print("\nOptions:")
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            library.display_available_books()
        elif choice == '2':
            book_to_borrow = input("Enter the name of the book you want to borrow: ")
            library.lend_book(book_to_borrow)
        elif choice == '3':
            book_to_return = input("Enter the name of the book you want to return: ")
            library.add_book(book_to_return)
        elif choice == '4':
            print("Thank you for using the library.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()