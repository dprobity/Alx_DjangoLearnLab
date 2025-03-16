from rest_framework import generics, viewsets, permissions 

#from rest_framework.generics import ListAPIView
from .models import Books
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    - Anyone can **view** books.
    - Only **authenticated users** can **add, update, or delete** books.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer

    # Apply permisions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



#  implementing custom permissions

# from .permissions import IsAdminOrReadOnly

# class BooksViewSet(viewsets.ModelViewSet):
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer

#     # Apply custom permission
#     permission_classes = [IsAdminOrReadOnly]



# this is the implementation for basic ListAPIView via the generics

# class BookList(generics.ListAPIView):
#     queryset = Books.objects.all()  # Retrieve all books from the database
#     serializer_class = BookSerializer  # Convert books to JSON format



