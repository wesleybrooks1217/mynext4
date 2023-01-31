from django.shortcuts import render
from rest_framework import viewsets
from .models import CareerSurveyOneAnswers
from .serializers import CareerSurveyOneAnswersSerializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CareerSurveyOneAnswersSerializer
from rest_framework import status
from rest_framework import views

# Create your views here.

class CareerSurveyOneAnswersView(viewsets.ModelViewSet):
    queryset = CareerSurveyOneAnswers.objects.all()
    serializer_class = CareerSurveyOneAnswersSerializer
    
    
    
    
 
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

