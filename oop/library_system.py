class Book:
    def __init__(self, title: str, author: str):
        """Base class for all books."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size_kb: int):
        """EBook inherits from Book and adds file_size."""
        super().__init__(title, author)  # Call base constructor
        self.file_size_kb = file_size_kb

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size_kb}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """PrintBook inherits from Book and adds page_count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library contains a collection of books."""
        self.books = []

    def add_book(self, book: Book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)

    def list_books(self):
        """Prints all books in the library."""
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)