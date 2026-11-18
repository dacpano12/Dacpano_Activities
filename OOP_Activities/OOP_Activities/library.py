class Book:
    # Class attribute — counts all books
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        Book.total_books += 1

    # Borrow method
    def borrow(self):
        if self.is_borrowed:
            return f"'{self.title}' is already borrowed!"
        self.is_borrowed = True
        return f"You borrowed '{self.title}'."

    # Return method
    def return_book(self):
        if not self.is_borrowed:
            return f"'{self.title}' is not borrowed."
        self.is_borrowed = False
        return f"You returned '{self.title}'."

    # String for users
    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"'{self.title}' by {self.author} — {status}"

    # String for developers
    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r})"


# Test the system
print("=== LIBRARY SYSTEM ===")
b1 = Book("Python Crash Course", "Eric Matthes")
b2 = Book("Clean Code", "Robert Martin")

print(f"\nTotal books: {Book.total_books}")
print("\n" + str(b1))
print(str(b2))

print("\n" + b1.borrow())
print(b2.borrow())
print(b1.borrow())  # Already borrowed

print("\n" + str(b1))
print(b1.return_book())
print(b1.return_book())  # Not borrowed

print("\nDeveloper view:")
print(repr(b1))
print(repr(b2))
