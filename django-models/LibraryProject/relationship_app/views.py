
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request,user)
            return redirect('list_books') # Redirect to an appropriate page
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})
        


# Function-based view to list all books with their authors
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, "relationship_app/list_books.html", {"books": books})

# Class-based view to display details for a specific library,
# including a list of all books available in that library.
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
    # Optionally, add the books related to this library to the context.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the books available in the library via the many-to-many field.
        context["books"] = self.object.books.all()
        return context

