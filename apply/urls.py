from django.urls import path
from .views import *


urlpatterns = [
    path('checkout/', checkOut, name = "checkOut"),
    path('checkin/', checkIn, name = "checkIn"),
    path('contact/', contact, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('registration_form/', registration_form, name='registration_form'),
    path('login/', student_login, name='student_login'),
    path('student/profile/', student_profile, name='student_profile'),
    path('forms/student/update/', student_update, name='student_update'),
    path('signout', signOut, name='signout')
]