from book import Book
from library import Library

if __name__ == "__main__":
    library = Library()
    
    # adding books
    book1 = Book("Harry Potter", "J.K. Rowling", 1997, "1234567890","harry-potter.txt")
    book2 = Book("The Hobbit", "J.R.R. Tolkien", 1937, "0987654321","hobbit.txt")
    library.add_book(book1)
    library.add_book(book2)
    
    # show available books
    library.show_available_books()
    
    # renting books
    print(library.rent_book("1234567890"))
    
    # show available books after renting
    library.show_available_books()
    
    # Zwracanie książki
    print(library.return_book("1234567890"))
    
    # show available books after renting
    library.show_available_books()
