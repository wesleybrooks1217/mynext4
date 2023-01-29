from django.urls import path
from .views import CareerSurveyOneView

urlpatterns = [
    path('survey/', CareerSurveyOneView.as_view({'get': 'get_survey'}), name='get_survey'),
    path('survey/submit/', CareerSurveyOneView.as_view({'get': 'submit_survey'}), name='submit_survey'),
]