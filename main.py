from book import Book
from library import Library

if __name__ == "__main__":
    library = Library()
    library.load_from_file("library_data.json")

    # Adding books
    book1 = Book("Harry Potter", "J.K. Rowling", 1997, "1234567890", "harry-potter.txt")
    book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "0987654321", "hobbit.txt")
    library.add_book(book1)
    library.add_book(book2)

    # Show available books
    library.show_available_books()

    # Renting books
    print(library.rent_book("1234567890"))

    # Show available books after renting
    library.show_available_books()

    # Returning books
    print(library.return_book("1234567890"))

    # Show available books after returning
    library.show_available_books()

    # Save the current state of the library to a file
    library.save_to_file("library_data.json")
