from django.urls import path
from .views import create_book, edit_book, delete_book

urlpatterns = [
    path('books/create/', create_book, name='create_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),
]


# from django.urls import path
# from django.contrib.auth import views as auth_views  
# # from .views import register,  list_books, LibraryDetailView, admin_view, librarian_view, member_view
# from . import views


# urlpatterns = [
#     # Route for the function-based view listing all books
#     path('books/', views.list_books, name='list_books'),
    
#     # Route for the class-based view to display a specific library's details.
#     # Here, <int:pk> is used to pass the primary key of the Library.
#     path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
#      # Authentication URLs using Django's built-in views
#     # path('login/', auth_views.LoginView.as_view(
#     #     template_name='registration/login.html',
#     #     redirect_authenticated_user=True,
#     #     next_page='/relationship_app/books/'  # Explicit redirect
#     # ), name='login'),    
#     # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),

#      # Authentication URLs
#     path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
#     path('logout/', auth_views.LogoutView.as_view(next_page='/relationship_app/login/'), name='logout'),
#     path('register/', views.register, name='register'),
#     path('admin/', views.admin_view, name='admin_view'),
#     path('librarian/', views.librarian_view, name='librarian_view'),
#     path('member/', views.member_view, name='member_view'),
# ]
