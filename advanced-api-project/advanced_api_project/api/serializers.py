from rest_framework import serializers
from .models import Book, Author



class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes validation to ensure the publication_year is not in the future.
    """

    class Meta:
        model = Book
        fields = '__all__'

    

    def validate_publication_year(self, value):
        from datetime import date
        if value > date.today().year:
            raise serializers.ValidationError("Publication year can not be in the future")
        return value



class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    - Includes the name field.
    - Uses a nested BookSerializer to serialize related book"
    """

    books = BookSerializer(many=True, read_only = True)

    class Meta:
        model = Author
        fields = ['name', 'books']