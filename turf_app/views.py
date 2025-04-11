from django.shortcuts import render
from .models import Slot, Booking
from datetime import date, datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from datetime import date, datetime, timedelta
from django.shortcuts import render
from turf_app.models import Slot

def available_slots(request):
    today = date.today()  # Get today's date
    tomorrow = today + timedelta(days=1)  # Get tomorrow's date
    now = datetime.now().time()  # Get the current time

    # Fetch slots for today (excluding past time slots)
    today_slots = Slot.objects.filter(date=today, start_time__gte=now).order_by('start_time')

    # Fetch slots for tomorrow
    tomorrow_slots = Slot.objects.filter(date=tomorrow).order_by('start_time')

    return render(request, 'turf_app/available_slots.html', {
        'today_slots': today_slots,
        'tomorrow_slots': tomorrow_slots
    })

from django.shortcuts import render, redirect, get_object_or_404
from .models import Slot, Booking
from django.contrib import messages

def book_slot(request, slot_id):
    slot = get_object_or_404(Slot, id=slot_id, is_available=True)  # Get the slot if available

    if request.method == 'POST':
        # Get customer details from the form
        customer_name = request.POST.get('customer_name')
        customer_number = request.POST.get('customer_number')

        # Create a new booking with the correct slot date
        booking = Booking.objects.create(
            customer_name=customer_name,
            customer_number=customer_number,
            slot=slot,
            booking_date=slot.date,  # Explicitly set the booking date to the slot's date
            amount=1500,  # Fixed amount
            payment_status='Completed'
        )

        # Mark the slot as unavailable
        slot.is_available = False
        slot.save()

        messages.success(request, f"Slot booked successfully for {slot.date} from {slot.start_time} to {slot.end_time}!")
        return redirect('available_slots')  # Redirect to the available slots page

    return render(request, 'turf_app/book_slot.html', {'slot': slot})

def view_bookings(request):
    bookings = Booking.objects.all().order_by('-booking_date')  # Fetch all bookings ordered by date (most recent first)
    return render(request, 'turf_app/view_bookings.html', {'bookings': bookings})