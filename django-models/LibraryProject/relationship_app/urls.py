from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Route for the function-based view listing all books
    path('books/', list_books, name='list_books'),
    
    # Route for the class-based view to display a specific library's details.
    # Here, <int:pk> is used to pass the primary key of the Library.
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
