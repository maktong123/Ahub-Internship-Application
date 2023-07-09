from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm

class CheckInForm(ModelForm):
    class Meta:
        model = Check_In
        fields = '__all__'

class CheckOutForm(ModelForm):
    class Meta:
        model = Check_Out
        fields = '__all__'

class BiodataForm(forms.ModelForm):
    class Meta:
        model = Biodata
        fields = [
            'first_name', 'other_names', 'gender', 'date_of_birth', 'start_date', 'end_date', 'phone_number',
            'school_name', 'state_of_origin', 'any_programming_skill', 'number_of_months',  'email_address','upload_photo',
            'upload_it_letter'
        ]



class StudentRegistrationForm(forms.Form):
    INTERNSHIP_TYPE_CHOICES = [
        ('Secondary', 'Secondary Internship Programs'),
        ('Undergraduate', 'Undergraduate Internship Programs'),
        ('Postgraduate', 'Postgraduate Internship Programs'),
    ]
    COURSES =[
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
    ('Male', 'Male'),
    ('Female', 'Female'),
    ]

    PROGRAMMING_SKILL_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
    ]
    first_name = forms.CharField(max_length=255)
    other_names = forms.CharField(max_length=255)  # Corrected field name
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    phone_number = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email_address = forms.EmailField()
    state_of_origin = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=255)
    school_name = forms.CharField(max_length=255)
    courses = forms.ChoiceField(choices=COURSES)
    any_programming_skill = forms.ChoiceField(choices=PROGRAMMING_SKILL_CHOICES)
    choose_internship_type = forms.ChoiceField(choices=INTERNSHIP_TYPE_CHOICES)  # Corrected field name
    number_of_months = forms.IntegerField()
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    upload_photo = forms.ImageField()
    upload_it_letter = forms.FileField()




class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class  ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))