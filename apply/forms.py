from django.forms import ModelForm
from .models import *

class CheckInForm(ModelForm):
    class Meta:
        model = Check_In
        fields = '__all__'

class CheckOutForm(ModelForm):
    class Meta:
        model = Check_Out
        fields = '__all__'