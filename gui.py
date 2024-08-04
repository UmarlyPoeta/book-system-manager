import tkinter as tk
from tkinter import ttk
from library import Library
# The `Book` class is likely a class that represents a book object in your library
# management system. It may contain attributes such as title, author, genre,
# publication year, availability status, etc., and methods to manipulate and retrieve
# information about a book object.
from book import Book
from sys import exit


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("Book System Manager")
        self.minsize(600, 600)
        self.configure(background='#f0f0f0')
        
        # Title Label
        title_label = ttk.Label(self, text="Book System Manager", font=("Roboto", 30), background='#f0f0f0')
        title_label.pack(pady=20)
        
        # Create a frame for the buttons
        button_frame = ttk.Frame(self, padding=10)
        button_frame.pack(pady=20)
        
        # Create a style for the buttons
        style = ttk.Style()
        style.configure('TButton', font=('Roboto', 12), padding=10)
        
        # Initialize library object
        library = Library()
        
        # Buttons
        buttons = [
            "[1] Load data from file",
            "[2] Save data to file",
            "[3] Exit",
            "[4] Add book",
            "[5] Show available books",
            "[6] Rent book",
            "[8] Help",
            "[9] About"
        ]
        ttk.Button(button_frame, command=lambda: library.load_from_file("library_data.json"), text=buttons[0], style='TButton').pack(pady=5, fill='x')
        ttk.Button(button_frame, command=lambda: library.save_to_file("library_data.json"),text=buttons[1], style='TButton').pack(pady=5, fill='x')
        ttk.Button(button_frame, command=lambda: exit(),text=buttons[2], style='TButton').pack(pady=5, fill='x')
        ttk.Button(button_frame, command=self.add_book,text=buttons[3], style='TButton').pack(pady=5, fill='x')
        ttk.Button(button_frame, command=self.show_books,text=buttons[4], style='TButton').pack(pady=5, fill='x')
        ttk.Button(button_frame, command=lambda: library,text=buttons[5], style='TButton').pack(pady=5, fill='x')
        ttk.Button(button_frame, text=buttons[6], style='TButton').pack(pady=5, fill='x')
        ttk.Button(button_frame, text=buttons[7], style='TButton').pack(pady=5, fill='x')
        
        
        self.mainloop()
        
    def add_book(self):
        pass
    
    def show_books(self):
        pass

if __name__ == "__main__":
    App()
