from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, datetime
from .models import *
from .forms import *
import pytz
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
# Create your views here.

def checkOut(request):
    checkRecordOut = Check_Out.objects.all()
    checkRecord = Check_In.objects.all()

    daysPresent = checkRecord.count()
    daysAbsent = Check_In.objects.filter(checkIn = None).count()
    checkForm = CheckOutForm()
    current_day = date.today()
    current_time = datetime.now().strftime("%H :%M")
    if request.method == "POST":
        # print('printing POST', request.POST)
        checkForm = CheckOutForm(request.POST)
        if checkForm.is_valid():
            checkForm.save()
            return redirect('/')
    context = {'form':checkForm, "current_day": current_day, 'time': current_time, "daysPresent" : daysPresent, "daysAbsent" : daysAbsent}

    return render(request, "check_out.html", context)

def checkIn(request):
    checkRecord = Check_In.objects.all()
    # daysPresent = checkRecord.count()
    daysPresent = checkRecord.count()
    daysAbsent = Check_In.objects.filter(checkIn = None).count()
    checkForm = CheckInForm()
    current_day = date.today()
    current_time = datetime.now().strftime("%H :%M")
    if request.method == "POST":
        # print('printing POST', request.POST)
        checkForm = CheckInForm(request.POST)
        if checkForm.is_valid():
            checkForm.save()
            return redirect('/')
    context = {'form':checkForm, "current_day": current_day, 'time': current_time, "daysPresent": daysPresent, "daysAbsent" : daysAbsent}
    return render(request, "check_in.html", context)

def registration_form(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data

            # Create User object
            user = User.objects.create_user(
                username=form_data['username'],
                password=form_data['password']
            )

            # Create Biodata object and associate it with the User
            biodata = Biodata.objects.create(
                user=user,
                first_name=form_data['first_name'],
                other_names=form_data['other_names'],
                gender=form_data['gender'],
                phone_number=form_data['phone_number'],
                date_of_birth=form_data['date_of_birth'],
                email_address=form_data['email_address'],
                password=form_data['password'],
                username=form_data['username'],
                state_of_origin=form_data['state_of_origin'],
                school_name=form_data['school_name'],
                courses=form_data['courses'],
                any_programming_skill=form_data['any_programming_skill'],
                choose_internship_type=form_data['choose_internship_type'],
                number_of_months=form_data['number_of_months'],
                start_date=form_data['start_date'],
                end_date=form_data['end_date'],
                upload_photo=request.FILES.get('upload_photo'),
                upload_it_letter=request.FILES.get('upload_it_letter')
            )
            biodata.save()
            messages.info(request, 'Registration Succesfully. Check Your Dashboard Status for Apporval')
            return redirect('student_login')  # Replace 'student_login' with the actual name/url of your login page
        else:
            # Form is not valid, print the errors
            print(form.errors)
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def signOut(request):
    logout(request)
    return redirect('student_login')

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_profile')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
        
@login_required
def student_update(request):
    if request.method == 'POST':
        form = BiodataForm(request.POST, request.FILES, instance=request.user.biodata)
        if form.is_valid():
            form.save()
            
            return redirect('student_profile')
    else:
        form = BiodataForm(instance=request.user.biodata) 
    
    return render(request, 'update_student.html', {'form': form})
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

@login_required
def student_profile(request):
    try:
        biodata = Biodata.objects.get(user=request.user)
        return render(request, 'profile.html', {'biodata': biodata})
    except Biodata.DoesNotExist:
        
        return render(request, 'profile.html', {'error_message': 'No biodata available'}, context)

def contact_success(request):
    return render(request, 'contact_success.html')
