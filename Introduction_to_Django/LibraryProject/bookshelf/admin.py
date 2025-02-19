from django.contrib import admin

# Register your models here.

from .models import Book

class Book_admin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('author', 'publication_year')  # Filters for easy search
    search_fields = ('title', 'author')  # Search bar for title and author
