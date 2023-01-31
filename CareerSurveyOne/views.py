from django import forms
from rest_framework import views
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QuestionSerializer
from .models import Question

from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.urls import reverse
from CareerSurveyOneAnswers.models import CareerSurveyOneAnswers
from CareerSurveyOneAnswers.serializers import CareerSurveyOneAnswersSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
# Create your views here.

class CareerSurveyOneView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class GetQuestionView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class =  QuestionSerializer
    def get_question(self, request, question_id, format=None):
        question = self.get_object()
        serializer = self.get_serializer(question)
        return Response(serializer.data)
       
       
      


        

class SubmitSurvey(views.APIView):
    def post(self, request, format=None):
        survey_data = request.data
        serializer = CareerSurveyOneAnswersSerializer(data=survey_data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)         

class GetSurvey(views.APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()    
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)