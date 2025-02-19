# Create a Book instance
from bookshelf.modles import Book

book - Book.objects.create(titlt="1984", author="George Orwell", publication_year=1949)
print(book)

# Expected Output:

<Book: 1984 by George Orwell (1949)>