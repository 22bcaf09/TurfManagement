from django.db import models

class Slot(models.Model):
    date = models.DateField()  # Date of the slot
    start_time = models.TimeField()  # Start time of the slot
    end_time = models.TimeField()  # End time of the slot
    is_available = models.BooleanField(default=True)  # Availability status

    def __str__(self):
        return f"{self.date} - {self.start_time.strftime('%I:%M %p')} to {self.end_time.strftime('%I:%M %p')}"
    
class Booking(models.Model):
    customer_name = models.CharField(max_length=100)  # Name of the customer
    customer_number = models.CharField(max_length=15)  # Contact number
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)  # Link to Slot table
    booking_date = models.DateField(auto_now_add=True)  # Date of booking
    amount = models.IntegerField(default=1500)  # Fixed amount
    payment_status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    ], default='Pending')  # Payment status

    def __str__(self):
        return f"Booking {self.id} - {self.customer_name}"
