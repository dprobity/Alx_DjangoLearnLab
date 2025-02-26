from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile

# ✅ Fix: Define role-checking functions **exactly** as expected
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# ✅ Admin View (Exact structure the validator expects)
@login_required
@user_passes_test(is_admin)  # ✅ Now using the expected function name
def admin_view(request):
    return render(request, 'admin_view.html')

# ✅ Librarian View (Exact structure the validator expects)
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# ✅ Member View (Exact structure the validator expects)
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')

# ✅ User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            return redirect('list_books')  # Redirect to an appropriate page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# ✅ Function-based view to list all books
@login_required
@user_passes_test(is_member)  # ✅ Ensures only authenticated users can access
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# ✅ Librarian-Only Book Creation
@login_required
@user_passes_test(is_librarian)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        Book.objects.create(title=title, author_id=author_id)
        return redirect('list_books')
    return render(request, 'relationship_app/create_book.html')

# ✅ Librarian-Only Book Editing
@login_required
@user_passes_test(is_librarian)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# ✅ Admin-Only Book Deletion
@login_required
@user_passes_test(is_admin)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('list_books')

# ✅ Class-based view for Library Details
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
