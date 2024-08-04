from book import Book
from library import Library
import os

def main_menu():
    print("=== Book System Manager ===")
    print("[1] Load data from file")
    print("[2] Save data to file")
    print("[3] Exit")
    print("[4] Add book")
    print("[5] Show available books")
    print("[6] Rent book")
    print("[7] Return book")
    print("[8] Help")
    print("[9] About")

def main():
    library = Library()

    while True:
        main_menu()
        choice = input("Choose an option: ")

        match choice:
            case "1":
                library.load_from_file("library_data.json")
                print("library was loaded")
            case "2":
                library.save_to_file("library_data.json")
                print("library was saved")
            case "3":
                break
            case "4":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = int(input("Enter release year: "))
                isbn = input("Enter ISBN: ")
                text_file_name = input("Enter text file name: ")
                book = Book(title, author, year, isbn, text_file_name)
                library.add_book(book)
                print("Book was added")
            case "5":
                for book in library.book_list:
                    if not book.rent:
                        print(book)
            case "6":
                isbn = input("Enter ISBN of the book to rent: ")
                print(library.rent_book(isbn))
            case "7":
                isbn = input("Enter ISBN of the book to return: ")
                print(library.return_book(isbn))
            case "8":
                print("Instructions on how to use the library manager.")
            case "9":
                print("Book System Manager v1.0. Created by Patryk.")
            case _:
                print("Invalid choice. Please try again.")
        input("press Enter")
        os.system("clear")

if __name__ == "__main__":
    main()
