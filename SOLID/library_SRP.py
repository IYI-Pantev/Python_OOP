class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

class BookSearch:
    @staticmethod
    def find_books_by_author(books, author):
        return [book for book in books if book.author == author]

class BookDisplay:
    @staticmethod
    def display_books(books):
        for book in books:
            print(book.title)

# Usage
books = [Book("Book 1", "Author A"), Book("Book 2", "Author B")]
library = Library(books)

author = "Author A"
author_books = BookSearch.find_books_by_author(library.books, author)
BookDisplay.display_books(author_books)
