from datetime import datetime, timedelta
from turf_app.models import Slot

def populate_slots_for_month(year, month):
    # Get the first and last day of the month
    start_date = datetime(year, month, 1).date()
    if month == 12:
        end_date = datetime(year + 1, 1, 1).date() - timedelta(days=1)
    else:
        end_date = datetime(year, month + 1, 1).date() - timedelta(days=1)

    # Loop through each day of the month
    current_date = start_date
    while current_date <= end_date:
        # Define the start and end time for slots
        start_time = datetime.strptime("08:00", "%H:%M").time()
        end_time = datetime.strptime("21:00", "%H:%M").time()

        # Create 1-hour slots for the day
        while start_time < end_time:
            Slot.objects.create(
                date=current_date,
                start_time=start_time,
                end_time=(datetime.combine(datetime.today(), start_time) + timedelta(hours=1)).time(),
                is_available=True
            )
            start_time = (datetime.combine(datetime.today(), start_time) + timedelta(hours=1)).time()

        current_date += timedelta(days=1)

    print(f"Slots populated for {month}/{year} successfully!")

# Call the function for the desired month and year
populate_slots_for_month(2025, 4)