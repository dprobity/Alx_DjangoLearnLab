from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer


# Create your views here.

class BookList(ListAPIView):
    queryset = Book.objects.all()              #  Retrieve all the books in the db
    serializer_class = BookSerializer           # Serialise or convert retrieved books to a JSON for the frontend to consume 

