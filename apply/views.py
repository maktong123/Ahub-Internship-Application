from django.shortcuts import render
from datetime import date, datetime
from .models import *
from .forms import *
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

