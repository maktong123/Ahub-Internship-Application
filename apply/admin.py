from django.contrib import admin
from .models import *
# Register your models here.
class BiodataAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'other_names', 'status']
    list_filter = ['status']
    
admin.site.register(Check_In)
admin.site.register(Check_Out)
admin.site.register(Biodata, BiodataAdmin)
admin.site.register(Contact)
