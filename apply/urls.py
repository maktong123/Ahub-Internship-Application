from django.urls import path
from .views import *


urlpatterns = [
    path('checkout/', checkOut, name = "checkOut"),
    path('checkin/', checkIn, name = "checkIn"),
]