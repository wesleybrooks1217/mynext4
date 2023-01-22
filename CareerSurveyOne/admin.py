from django.contrib import admin
from .models import CareerSurveyOne

# Register your models here.

class CareerSurveyOneAdmin(admin.ModelAdmin):
    list_display = (
        'question'
    )

admin.site.register(CareerSurveyOne, CareerSurveyOneAdmin)