from django.db import models

class Slot(models.Model):
    date = models.DateField()  # Date of the slot
    start_time = models.TimeField()  # Start time of the slot
    end_time = models.TimeField()  # End time of the slot
    is_available = models.BooleanField(default=True)  # Availability status

    def __str__(self):
        return f"{self.date} - {self.start_time.strftime('%I:%M %p')} to {self.end_time.strftime('%I:%M %p')}"