from typing import List

from booksearch.model.book import Book, BookItem


class InventoryService:
    def __init__(self):
        self.books: List[BookItem] = []

    def add_book(self, book: BookItem):
        self.books.append(book)

    def remove_book(self, book: BookItem):
        self.books.remove(book)
