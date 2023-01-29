from django.contrib import admin
from .models import CareerSurveyOne



class CareerSurveyOneAdmin(admin.ModelAdmin):
    list_display = ('secondary_school', 'tertiary_school', 'independent_job', 'work_from_home', 'favorite_subject', 'favorite_careers', 'shifting_schedule', 'socializing_more', 'sports_as_career', 'travel_for_work')

admin.site.register(CareerSurveyOne)