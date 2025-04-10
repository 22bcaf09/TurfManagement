from django.shortcuts import render
from .models import Slot
from datetime import date, datetime

def available_slots(request):
    today = date.today()  # Get today's date
    now = datetime.now().time()  # Get the current time

    # Filter slots for today and exclude past time slots
    slots = Slot.objects.filter(is_available=True, date=today, start_time__gte=now).order_by('start_time')

    return render(request, 'turf_app/available_slots.html', {'slots': slots})