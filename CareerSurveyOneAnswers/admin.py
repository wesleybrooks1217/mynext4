from django.contrib import admin
from .models import CareerSurveyOneAnswers



class CareerSurveyOneAnswersAdmin(admin.ModelAdmin):
    list_display = ('survey_id', 'user_id', 'question', 'answer')
admin.site.register(CareerSurveyOneAnswers)