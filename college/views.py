from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CollegeSerializer
from .models import College

# Create your views here.

class CollegeView(viewsets.ModelViewSet):
    serializer_class = CollegeSerializer
    queryset = College.objects.all()
