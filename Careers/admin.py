from django.contrib import admin
from .models import Career
# Register your models here.



class CareerAdmin(admin.ModelAdmin):
    list_display = (
    'career_name',
    'onet_id',
    'median_salary',
    'industry',
    'id',
    'education')




admin.site.register(Career, CareerAdmin)
