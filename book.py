class Book:
    def __init__(self, title: str, author: str, release_year: int, isbn: str, text_file_name: str, rent: bool = False) -> None:
        self.title: str = title
        self.author: str = author
        self.year: int = release_year
        self.isbn: str = isbn
        self.rent: bool = rent

        try:
            with open(text_file_name, "r") as book_representation:
                self.text_representation: list[str] = book_representation.readlines()
        except OSError as e:
            print(f"Error opening file {text_file_name}: {e}")
            self.text_representation = []

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "isbn": self.isbn,
            "rent": self.rent,
            "text_representation": self.text_representation
        }

    @classmethod
    def from_dict(cls, data: dict):
        book = cls(data["title"], data["author"], data["year"], data["isbn"], "")
        book.rent = data["rent"]
        book.text_representation = data["text_representation"]
        return book

    def __str__(self) -> str:
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Year: {self.year}\n"
                f"ISBN: {self.isbn}\n"
                f"Text preview: {''.join(self.text_representation[:10])}")
