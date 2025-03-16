from rest_framework import serializers
from . models import Book, Events, Ticket


class BookSerializer(serializers.ModelSerializer):
    days_since_created = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'created_at', 'days_since_created']
        fields = '__all__'
        def get_days_since_created(self, obj):
            from  datetime import datetime, timezone
            return (datetime.now(timezone.utc) - obj.created_at).days
        
        
    



class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    """Serializer for the Ticket model."""
    event_name = serializers.ReadOnlyField(source="event.name")  # Include event name in response

    class Meta:
        model = Ticket
        fields = ['id', 'event', 'event_name', 'buyer_name', 'email', 'purchase_date']
