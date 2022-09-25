from django.shortcuts import render
from rest_framework import viewsets
from .serializers import highSchoolCoursesSerializer
from .models import highSchoolCourses

# Create your views here.

class highSchoolCoursesView(viewsets.ModelViewSet):
    serializer_class = highSchoolCoursesSerializer
    queryset = highSchoolCourses.objects.all()
