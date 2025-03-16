from rest_framework import generics, viewsets

#from rest_framework.generics import ListAPIView
from .models import Books
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """A viewset for viewing an deditiing book instances."""

    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookList(generics.ListAPIView):
    queryset = Books.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Convert books to JSON format



