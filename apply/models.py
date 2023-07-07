from django.db import models
from django.utils import timezone

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
