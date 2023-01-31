from django.contrib import admin
from .models import CareerSurveyOneAnswers



class CareerSurveyOneAnswersAdmin(admin.ModelAdmin):
    list_display = ('userID', 'questionID', 'answer')
admin.site.register(CareerSurveyOneAnswers, CareerSurveyOneAnswersAdmin)