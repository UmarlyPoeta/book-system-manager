class Book:
    def __init__(self,title: str, author: str, release_year: int, isbn: str, text_file_name: str) -> None | OSError:
        self.title: str = title
        self.author: str = author
        self.year: int = release_year
        self.isbn: str = isbn
        self.rent: bool = False
        
        
        try:
            with open(text_file_name,"r") as book_representation:
                self.text_representation: list[str] = book_representation.readlines()
        except OSError:
            return OSError("File does not exist")
    
    def __str__(self) -> str:
        print(f"title: {self.title}")
        print(f"author: {self.author}")
        print(f"release_year: {self.year}")
        print(f"isbn: {self.isbn}\n\n")

        print("Here is a glimpse of a book :)\n\n")
        try:
            return "".join(self.text_representation[:10])
        except IndexError:
            return "".join(self.text_representation)

