from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Check_In(models.Model):
    checkIn = models.BooleanField(default=True)
    dateCheckedIn = models.DateTimeField(default="Date Checked In")

    def __str__(self):
        if(self.checkIn):
            return "SIGN IN at  " + str(self.dateCheckedIn)
        return "NOT SIGNED IN"
    
class Check_Out(models.Model):
    checkOutText = models.TextField(max_length=300, blank=True, null=True)
    check_out = models.BooleanField(default=False)
    dateCheckedOut = models.DateTimeField(default="Date Checked In")
    def __str__(self):
        return "SIGNED OUT at " + str(self.dateCheckedOut)

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    INTERNSHIP_TYPE_CHOICES = [
        ('secondary', 'Secondary Internship Programs'),
        ('undergraduate', 'Undergraduate Internship Programs'),
        ('postgraduate', 'Postgraduate Internship Programs'),
    ]
    COURSES = [
        ('SWeb Development', 'Web Development'),
        ('App Development', 'App Development'),
        ('Data Science', 'Data Science'),
        ('Digital Marketing', 'Digital Marketing'),
        ('Content Management', 'Content Management'),
        ('UX/UI Design', 'UX/UI Design'),
        ('Graphic Design', 'Graphic Design'),
        ('Mentorship', 'Mentorship'),     
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    PROGRAMMING_SKILL_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]
    # existing fields
    first_name = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    email_address = models.EmailField()
    state_of_origin = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    school_name = models.CharField(max_length=255)
    courses = models.CharField(max_length=100, choices=COURSES)
    any_programming_skill = models.CharField(max_length=10, choices=PROGRAMMING_SKILL_CHOICES)
    choose_internship_type = models.CharField(max_length=100, choices=INTERNSHIP_TYPE_CHOICES)
    number_of_months = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    upload_photo = models.ImageField(upload_to='photos/')
    upload_it_letter = models.FileField(upload_to='it_letters/')
    
    # New field for admission status
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.first_name + ' ' + self.other_names


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name