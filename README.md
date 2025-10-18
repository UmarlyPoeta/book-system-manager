# Book System Manager

A Python-based library management system that allows users to manage a collection of books with both command-line interface (CLI) and graphical user interface (GUI) options.

## Features

- **Add Books**: Add new books to your library with title, author, year, ISBN, and text content
- **Rent Books**: Track which books are currently rented out
- **Return Books**: Mark books as returned and available again
- **View Available Books**: See all books that are currently available (not rented)
- **Persistent Storage**: Save and load library data from JSON files
- **Text Preview**: Store and display book text content with preview functionality
- **Dual Interface**: Choose between CLI or GUI operation modes

## Requirements

- Python 3.10 or higher (uses match-case syntax)
- tkinter (usually included with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/UmarlyPoeta/book-system-manager.git
cd book-system-manager
```

2. Ensure you have Python 3.10+ installed:
```bash
python --version
```

3. No additional dependencies are required - the project uses only Python standard library modules!

## Usage

### Command-Line Interface (CLI)

To run the CLI version:

```bash
python main.py
```

#### Available Options:

1. **Load data from file** - Load existing library data from `library_data.json`
2. **Save data to file** - Save current library state to `library_data.json`
3. **Exit** - Close the application
4. **Add book** - Add a new book by entering:
   - Title
   - Author
   - Release year
   - ISBN
   - Text file name (or leave empty)
5. **Show available books** - Display all books that are not currently rented
6. **Rent book** - Rent a book by entering its ISBN
7. **Return book** - Return a rented book by entering its ISBN
8. **Help** - Display instructions
9. **About** - Show application information

### Graphical User Interface (GUI)

To run the GUI version:

```bash
python gui.py
```

The GUI provides a modern interface with buttons for the main operations.

## Project Structure

```
book-system-manager/
├── book.py                      # Book class definition
├── library.py                   # Library class for managing book collections
├── main.py                      # CLI application entry point
├── gui.py                       # GUI application (in development)
├── library_data.json            # Sample library data file
├── example_book_txt_files/      # Sample book text files
│   ├── harry-potter.txt
│   └── hobbit.txt
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## How It Works

### Book Class (`book.py`)

The `Book` class represents individual books with the following attributes:
- `title`: Book title
- `author`: Author name
- `year`: Publication year
- `isbn`: ISBN number (used as unique identifier)
- `rent`: Boolean indicating if the book is currently rented
- `text_representation`: List of lines from the book's text file

### Library Class (`library.py`)

The `Library` class manages a collection of books with methods to:
- Add books (with ISBN uniqueness validation)
- Rent and return books
- Save/load library data to/from JSON files
- Display available books

### Data Format

Library data is stored in JSON format with the following structure:

```json
[
    {
        "title": "Book Title",
        "author": "Author Name",
        "year": 1997,
        "isbn": "1234567890",
        "rent": false,
        "text_representation": ["Line 1", "Line 2", "..."]
    }
]
```

## Example Workflow

1. Start the application: `python main.py`
2. Load existing data: Choose option `[1]`
3. View available books: Choose option `[5]`
4. Rent a book: Choose option `[6]` and enter the ISBN
5. Return a book: Choose option `[7]` and enter the ISBN
6. Add a new book: Choose option `[4]` and follow the prompts
7. Save your changes: Choose option `[2]`
8. Exit: Choose option `[3]`

## Sample Data

The repository includes sample data with two books:
- **Harry Potter and the Sorcerer's Stone** by J.K. Rowling (1997)
- **The Hobbit** by J.R.R. Tolkien (1937)

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## Future Enhancements

- Complete GUI implementation
- Search functionality (by title, author, or ISBN)
- Book categories/genres
- User management system
- Due dates for rentals
- Late fee calculation
- Book recommendations

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created by Patryk

## Version

Book System Manager v1.0
