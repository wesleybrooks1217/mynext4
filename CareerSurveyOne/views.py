from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CareerSurveyOneSerializer
from .models import CareerSurveyOne

# Create your views here.

class CareerSurveyOneView(viewsets.ModelViewSet):
    serializer_class = CareerSurveyOneSerializer
    queryset = CareerSurveyOne.objects.all()
    
