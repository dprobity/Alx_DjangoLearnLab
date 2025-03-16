import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
django.setup()

from api.models import Books

# Add books
books = [
    {"title": "The Alchemist", "author": "Paulo Coelho"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"title": "1984", "author": "George Orwell"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"}
]

for book in books:
    obj, created = Books.objects.get_or_create(title=book["title"], author=book["author"])
    if created:
        print(f'Added: {book["title"]} by {book["author"]}')
    else:
        print(f'Skipped (already exists): {book["title"]} by {book["author"]}')

# Show all books in the database
print("\nCurrent Books in Database:")
for book in Books.objects.all():
    print(f'{book.id}. {book.title} - {book.author}')
