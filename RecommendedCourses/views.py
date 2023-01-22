from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecommendedCoursesSerializer
from .models import RecommendedCourses

# Create your views here.
class RecommendedCoursesView(viewsets.ModelViewSet):
    serializer_class = RecommendedCoursesSerializer
    queryset = RecommendedCourses.objects.all()
