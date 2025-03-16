from rest_framework import generics
#from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Convert books to JSON format
