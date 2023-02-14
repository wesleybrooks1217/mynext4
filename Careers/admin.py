from django.contrib import admin
from .models import Career
# Register your models here.



class CareerAdmin(admin.ModelAdmin):
    list_display = (
    'name',
    'onetID')




admin.site.register(Career, CareerAdmin)
