from django.urls import path
from .views import EventListCreateView, TicketListCreateView

urlpatterns = [
    path("events/", EventListCreateView.as_view(), name="event-list"),
    path("events/<int:event_id>/tickets/", TicketListCreateView.as_view(), name="ticket-list"),
]
