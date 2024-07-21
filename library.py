import json
from book import Book

class Library:
    def __init__(self) -> None:
        self.book_list: list[Book] = []

    def add_book(self, book: Book) -> None:
        try:
            self.check_if_isbn_in_book_list(book.isbn)
        except ValueError as e:
            print("The book with that isbn was already added")
            return None
        self.book_list.append(book)

    def check_if_isbn_in_book_list(self, isbn: str) -> None | ValueError:
        if isbn in [book.isbn for book in self.book_list]:
            raise ValueError
        return None

    def rent_book(self, isbn: str) -> str:
        for book in self.book_list:
            if book.isbn == isbn:
                if not book.rent:
                    book.rent = True
                    return f"Book '{book.title}' was rented"
                return f"Book '{book.title}' was already rented"
        return f"No book with ISBN {isbn} was found"

    def return_book(self, isbn: str) -> str:
        for book in self.book_list:
            if book.isbn == isbn:
                if book.rent:
                    book.rent = False
                    return f"Book '{book.title}' was returned"
                return f"Book '{book.title}' was never rented"
        return f"No book with ISBN {isbn} was found"

    def show_available_books(self) -> None:
        if not self.book_list:
            print("There are no books available :(")
            return

        print("List of available books:\n")
        for book in self.book_list:
            if not book.rent:
                print(book)

    def save_to_file(self, filename: str) -> None:
        with open(filename, "w") as file:
            json.dump([book.to_dict() for book in self.book_list], file, indent=4)

    def load_from_file(self, filename: str) -> None:
        try:
            with open(filename, "r") as file:
                books_data = json.load(file)
                self.book_list = [Book.from_dict(data) for data in books_data]
        except FileNotFoundError:
            print(f"No file named {filename} found. Starting with an empty library.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}. Starting with an empty library.")
