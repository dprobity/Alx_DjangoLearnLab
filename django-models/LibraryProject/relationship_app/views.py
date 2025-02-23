
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
# Create your views here.


# Function-based view to list all books with their authors
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, "list_books.html", {"books": books})

# Class-based view to display details for a specific library,
# including a list of all books available in that library.
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
    
    # Optionally, add the books related to this library to the context.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the books available in the library via the many-to-many field.
        context["books"] = self.object.books.all()
        return context

