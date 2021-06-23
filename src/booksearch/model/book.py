class Book:
    def __init__(self, book_id, book_title, book_genre, book_publisher, book_author):
        self.book_id = book_id
        self.book_title = book_title
        self.book_genre = book_genre
        self.book_publisher = book_publisher
        self.book_author = book_author


class BookItem(Book):
    def __init__(self, book_id, book_title, book_genre, book_publisher, book_author, isbn_code):
        super().__init__(book_id, book_title, book_genre, book_publisher, book_author)
        self.isbn_code = isbn_code
