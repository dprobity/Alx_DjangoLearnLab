from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()



class Events(models.Model):
    """Event model representing an event."""
    name = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Ticket(models.Model):
    """Ticket model representing  a ticket purchase for an event."""
    event = models.ForeignKey(Events, on_delete=models.CASCADE, related_name="tickets" )
    buyer_name = models.CharField(max_length=255)
    email = models.EmailField()
    purchase_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.event.name} - {self.buyer_name}"
