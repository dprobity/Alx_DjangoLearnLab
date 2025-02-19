# Delete the book instance
retrieved_book.delete()

# Confirm deletion
books = Book.objects.all()
print(list(books))

# Expected Output

[]  # Empty list, meaning no books exist in the database