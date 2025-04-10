from django.shortcuts import render
from .models import Slot, Booking
from datetime import date, datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from collections import defaultdict

def available_slots(request):
    today = date.today()  # Get today's date
    now = datetime.now().time()  # Get the current time

    # Filter slots for today and exclude past time slots
    slots = Slot.objects.filter(is_available=True, date=today, start_time__gte=now).order_by('start_time')

    return render(request, 'turf_app/available_slots.html', {'slots': slots})

def book_slot(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id, is_available=True)  # Get the slot if available

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_number = request.POST.get('customer_number')

        # Create a new booking
        Booking.objects.create(
            customer_name=customer_name,
            customer_number=customer_number,
            slot=slot,
            amount=1500,  # Fixed amount
            payment_status='Pending'
        )

        # Mark the slot as unavailable
        slot.is_available = False
        slot.save()

        messages.success(request, 'Slot booked successfully!')
        return redirect('available_slots')  # Redirect to the available slots page

    return render(request, 'turf_app/book_slot.html', {'slot': slot})

def view_bookings(request):
    bookings = Booking.objects.all().order_by('-booking_date')  # Fetch all bookings ordered by date (most recent first)
    return render(request, 'turf_app/view_bookings.html', {'bookings': bookings})