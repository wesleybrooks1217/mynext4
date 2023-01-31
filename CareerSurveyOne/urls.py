
from django.urls import path

from .views import SubmitSurvey, GetSurvey, CareerSurveyOneView, GetQuestionView
from rest_framework.response import Response
from rest_framework import status






urlpatterns = [
    path('submit/', SubmitSurvey.as_view(), name='submit_survey'),
    path('', GetSurvey.as_view(), name='get_survey'),
    path('<int:pk>/', GetQuestionView.as_view(), name='get_question'),
]
