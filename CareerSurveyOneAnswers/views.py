from django.shortcuts import render
from rest_framework import viewsets
from .models import CareerSurveyOneAnswers
from .serializers import CareerSurveyOneAnswersSerializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import CareerSurveyOne
from .serializers import CareerSurveyOneAnswersSerializer
from CareerSurveyOne.forms import CareerSurveyOneForm
from rest_framework import status

# Create your views here.

class CareerSurveyOneAnswersView(viewsets.ModelViewSet):
    queryset = CareerSurveyOneAnswers.objects.all()
    serializer_class = CareerSurveyOneAnswersSerializer
    def create(self, request, *args, **kwargs):
        form = CareerSurveyOneForm(request.data)
        if form.is_valid():
            survey = form.save()
            serializer = self.get_serializer(survey)
            return Response(serializer.data)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        form = CareerSurveyOneForm(request.data, instance=instance)
        if form.is_valid():
            survey = form.save()
            serializer = self.get_serializer(survey)
            return Response(serializer.data)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)