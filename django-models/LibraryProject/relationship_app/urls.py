from django.urls import path
from django.contrib.auth import views as auth_views  
from .views import register,  list_books, LibraryDetailView


urlpatterns = [
    # Route for the function-based view listing all books
    path('books/', list_books, name='list_books'),
    
    # Route for the class-based view to display a specific library's details.
    # Here, <int:pk> is used to pass the primary key of the Library.
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
     # Authentication URLs using Django's built-in views
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        redirect_authenticated_user=True,
        next_page='/relationship_app/books/'  # Explicit redirect
    ), name='login'),    
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', register, name='register'),
]
