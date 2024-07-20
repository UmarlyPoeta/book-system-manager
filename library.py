class Library:
    def __init__(self) -> None:
        self.book_list: list[object] = []
    
    def add_book(self, book) -> None:
        self.book_list.append(book)
    
    def rent_book(self,isbn: str) -> str:
        for book in self.book_list:
            if book.isbn == isbn:
                if not book.rent:
                    book.rent = True
                    return f"Book {book.title} was rented\n"
                return f"Book {book.title} was already rented\n"
        return f"No book with isbn {isbn} was found\n"
    
    def return_book(self, isbn: str) -> str:
        for book in self.book_list:
            if book.isbn == isbn:
                if book.rent:
                    book.rent = False
                    return f"Book {book.title} was returned\n"
                return f"Book {book.title} was never rented\n"
        return f"No book with isbn {isbn} was found\n"
    
    def show_available_books(self) -> None:
        print("List of books available:\n")
        if not self.book_list:
            print("There is no book available :()")
        else:
            for book in self.book_list:
                if not book.rent:
                    print(book)