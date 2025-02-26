
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

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile

# ✅ Define role-checking functions directly in views.py (instead of decorators.py)
def user_is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def user_is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# ✅ Admin View (Restricted to Admins)
@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

# ✅ Librarian View (Restricted to Librarians)
@login_required
@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

# ✅ Member View (Restricted to Members)
@login_required
@user_passes_test(user_is_member)
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
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, "relationship_app/list_books.html", {"books": books})

# ✅ Class-based view to display details for a specific library
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
