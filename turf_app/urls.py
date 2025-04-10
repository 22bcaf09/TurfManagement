from django.urls import path
from . import views

urlpatterns = [
    path('available-slots/', views.available_slots, name='available_slots'),
    path('book-slot/<int:slot_id>/', views.book_slot, name='book_slot'),
    path('view-bookings/', views.view_bookings, name='view_bookings'),
]