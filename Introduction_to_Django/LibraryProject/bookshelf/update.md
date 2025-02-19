# Update the book title and save changes
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Verify update
updated_book = Book.objects.get(id=retrieved_book.id)
print(f"Updated Title: {updated_book.title}")

# Expected Output
<Updated Title: Nineteen Eighty-Four>