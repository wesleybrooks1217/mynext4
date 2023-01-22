from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CoursesSerializer
from .models import Courses

# Create your views here.

class CoursesView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
