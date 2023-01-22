from django.contrib import admin
from .models import CareerSurveyOneAnswers

# Register your models here.

class CareerSurveyOneAnswerAdmin(admin.ModelAdmin):
    list_display = (
        'questionID',
        'userID',
        'answer'
    )

admin.site.register(CareerSurveyOneAnswers, CareerSurveyOneAnswerAdmin)