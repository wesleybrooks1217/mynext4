from django import forms
from .models import CareerSurveyOne

class CareerSurveyOneForm(forms.ModelForm):
    class Meta:
        model = CareerSurveyOne
        fields = ['secondary_school', 'tertiary_school', 'independent_job', 'work_from_home', 'favorite_subject', 'favorite_careers', 'shifting_schedule', 'socializing_more', 'sports_as_career', 'travel_for_work']
