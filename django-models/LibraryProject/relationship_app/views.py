from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import  permission_required # ✅ Add this exact import
from django.contrib.auth.decorators import  login_required  # ✅ Add this exact import

from .models import Book

# ✅ Create Book (Only users with 'can_add_book' permission)
@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        Book.objects.create(title=title, author_id=author_id)
        return redirect('list_books')
    return render(request, 'relationship_app/create_book.html')

# ✅ Edit Book (Only users with 'can_change_book' permission)
@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('list_books')
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# ✅ Delete Book (Only users with 'can_delete_book' permission)
@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('list_books')
