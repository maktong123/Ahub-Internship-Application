from django.contrib import admin

# Register your models here.
from .models import *
class imageAdmin(admin.ModelAdmin):
    list_display = ["firstName","otherName", "phone", "email", "photo",  "date_created"]
admin.site.register(StaffList, imageAdmin)
admin.site.register(Proficiency)
admin.site.register(Role)