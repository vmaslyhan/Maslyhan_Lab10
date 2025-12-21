from django.shortcuts import render
from .models import Guest, Room, Registration

def index(request):
    guests = Guest.objects.all()
    rooms = Room.objects.all()
    registrations = Registration.objects.select_related("guest", "room")

    context = {
        "project_name": "Готель",
        "student": "Маслиган Віталій Романович, ІПЗ-22009б",
        "guests": guests,
        "rooms": rooms,
        "registrations": registrations,
    }

    return render(request, "index.html", context)
