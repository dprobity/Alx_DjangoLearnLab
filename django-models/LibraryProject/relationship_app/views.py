
# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic.detail import DetailView
# from .models import Book
# from .models import Library
# # Create your views here.

# from django.contrib.auth.decorators import login_required, user_passes_test
# from .decorators import user_is_admin, user_is_librarian, user_is_member

# # ✅ Admin View
# @login_required
# @user_passes_test(user_is_admin)
# def admin_view(request):
#     return render(request, 'admin_view.html')

# # ✅ Librarian View
# @login_required
# @user_passes_test(user_is_librarian)
# def librarian_view(request):
#     return render(request, 'librarian_view.html')

# # ✅ Member View
# @login_required
# @user_passes_test(user_is_member)
# def member_view(request):
#     return render(request, 'member_view.html')


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # Log the user in after registration
#             login(request,user)
#             return redirect('list_books') # Redirect to an appropriate page
#     else:
#         form = UserCreationForm()
#         return render(request, 'registration/register.html', {'form': form})
        


# # Function-based view to list all books with their authors
# def list_books(request):
#     books = Book.objects.all()  # Query all books
#     return render(request, "relationship_app/list_books.html", {"books": books})

# # Class-based view to display details for a specific library,
# # including a list of all books available in that library.
# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = "relationship_app/library_detail.html"
#     context_object_name = "library"
    
#     # Optionally, add the books related to this library to the context.
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # Retrieve the books available in the library via the many-to-many field.
#         context["books"] = self.object.books.all()
#         return context



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from .decorators import admin_required, librarian_required, member_required

# ✅ Admin View (Restricted to Admins)
@login_required
@admin_required
def admin_view(request):
    return render(request, 'admin_view.html')

# ✅ Librarian View (Restricted to Librarians)
@login_required
@librarian_required
def librarian_view(request):
    return render(request, 'librarian_view.html')

# ✅ Member View (Restricted to Members)
@login_required
@member_required
def member_view(request):
    return render(request, 'member_view.html')

# ✅ User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            return redirect('list_books')  # Redirect to an appropriate page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# ✅ Function-based view to list all books with their authors
@login_required
@member_required  # ✅ Only Members, Librarians, and Admins can view books
def list_books(request):
    books = Book.objects.all()  
    return render(request, "relationship_app/list_books.html", {"books": books})

# ✅ Librarian-Only Book Creation
@login_required
@librarian_required
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        Book.objects.create(title=title, author_id=author_id)
        return redirect('list_books')
    return render(request, 'relationship_app/create_book.html')

# ✅ Librarian-Only Book Editing
@login_required
@librarian_required
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# ✅ Admin-Only Book Deletion
@login_required
@admin_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('list_books')

# ✅ Class-based view for Library Details (Restricted to Members)
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
