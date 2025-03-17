from django.db import models

# Create your models here.

class Author(models.Model):
    """ 
    Model representing an author.
    - name: stores the author's anme.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    



class Book(models.Model):
    """
    Model rep a book.
    - title: Stores the book's title.
    - publication_year : Stores the year the book was published.
    - author: Establishes a foreign key relationship to the authors model.
    """

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title






