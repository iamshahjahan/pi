from booksearch.model.book import Book


class TypeAheadSearchService:
    def __init__(self):
        self.__title_dict = {}
        self.__publisher_dict = {}
        self.__author_dict = {}

    def add_title(self, book: Book):
        self.__title_dict[book.book_title] = [book]

    def add_publisher(self, book: Book):
        self.__publisher_dict[book.book_publisher] = self.__publisher_dict.get(book.book_publisher, []).append(book)

    def add_author(self, book: Book):
        self.__publisher_dict[book.book_author] = self.__publisher_dict.get(book.book_author, []).append(book)

    def delete_title(self, book: Book):
        del self.__title_dict[book.book_title]

    def delete_publisher(self, book: Book):

        for publisher, books in self.__publisher_dict.items():
            if publisher == book.book_publisher:
                books.pop(book)

    def delete_author(self, book: Book):
        for author, books in self.__publisher_dict.items():
            if author == book.book_author:
                books.pop(book)
