from django.db import models

# Create your models here.
class Proficiency(models.Model):
    name = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name
    
class Role(models.Model):
    name = models.CharField(max_length=150, null=True)
    def __str__(self):
        return self.name
    
class StaffList(models. Model):
    firstName = models.CharField(max_length=150, null=True)
    otherName = models.CharField(max_length=150, null= True)
    phone = models.CharField(max_length=150, null=True)
    email = models.EmailField(max_length= 150, null=True, blank=True)
    role = models.ManyToManyField(Role)
    photo = models.ImageField(blank= True, null=True, upload_to= "images/")
    proficiency = models.ManyToManyField(Proficiency)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.firstName
