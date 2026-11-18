class Book:
    # Class attribute — count ALL books in the library
    total_books = 0

    def __init__(self, title, author):
        # Instance attributes — unique to each book
        self.title = title
        self.author = author
        self.is_borrowed = False  # Track availability
        Book.total_books += 1     # Increment counter when new book is created

    # Method 1: Borrow the book
    def borrow(self):
        if self.is_borrowed:
            return f"❌ '{self.title}' is already borrowed!"
        self.is_borrowed = True
        return f"✅ You borrowed '{self.title}'."

    # Method 2: Return the book
    def return_book(self):
        if not self.is_borrowed:
            return f"ℹ️ '{self.title}' is not borrowed."
        self.is_borrowed = False
        return f"✅ You returned '{self.title}'."

    # For users — readable format
    def __str__(self):
        status = "📖 Borrowed" if self.is_borrowed else "✅ Available"
        return f"'{self.title}' by {self.author} — {status}"

    # For developers — detailed representation
    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r})"


# === TEST THE LIBRARY SYSTEM ===
print("=" * 50)
print("      📚 LIBRARY BOOK SYSTEM")
print("=" * 50)

# Create books
book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Clean Code", "Robert C. Martin")
book3 = Book("The Alchemist", "Paulo Coelho")

# Show total books
print(f"\nTotal books in library: {Book.total_books}")

# Show all books
print("\n--- All Books ---")
print(book1)
print(book2)
print(book3)

# Borrow some books
print("\n--- Borrowing Books ---")
print(book1.borrow())
print(book2.borrow())
print(book1.borrow())  # Try borrowing again — should fail

# Check status
print("\n--- Status After Borrowing ---")
print(book1)
print(book2)
print(book3)

# Return a book
print("\n--- Returning Book ---")
print(book1.return_book())
print(book1.return_book())  # Try returning again — should inform

# Final status
print("\n--- Final Status ---")
print(book1)
print(book2)
print(book3)

print("\n--- Developer View (using __repr__) ---")
print(repr(book1))
print(repr(book2))
