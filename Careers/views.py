from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SkillsSerializer, IndustrySerializer, CareerSerializer, StateSerializer
from .models import Skills, Industry, Career, States


class SkillsView(viewsets.ModelViewSet):
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()

class IndustryView(viewsets.ModelViewSet):
    serializer_class = IndustrySerializer
    queryset = Industry.objects.all()

class CareerView(viewsets.ModelViewSet):
    serializer_class = CareerSerializer
    queryset = Career.objects.all()

class StatesView(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = States.objects.all()

# Create your views here.
