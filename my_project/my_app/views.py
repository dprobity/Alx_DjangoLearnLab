from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventsSerializer, TicketSerializer, BookSerializer
from .models import *



class EventListCreateView(APIView):
    """View to list all events or create a new event."""

    def get(self, request):
        events = Events.objects.all()
        serializer = EventsSerializer(events, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EventsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketListCreateView(APIView):
    """View to list tickets for an event and allow ticket purchases."""

    def get(self, request, event_id=None):
        """Retrieve tickets for a specific events"""
        if event_id is None:
            return Response({"error": "Event ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        tickets = Ticket.objects.filter(event_id= event_id)
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)


    def post(self, request, event_id):
        """Allow a user to buy a ticket for an event."""
        request.data['event'] = event_id # Attach an event id to the ticket
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
