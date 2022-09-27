from django.shortcuts import render
from rest_framework import viewsets
from .serializers import duelEnrollmentCoursesSerializer, duelEnrollmentSchoolSerializer
from .models import duelEnrollmentCourses, duelEnrollmentSchool

class duelEnrollmentCoursesView(viewsets.ModelViewSet):
    serializer_class = duelEnrollmentCoursesSerializer
    queryset = duelEnrollmentCourses.objects.all()

class duelEnrollmentSchoolView(viewsets.ModelViewSet):
    serializer_class = duelEnrollmentSchoolSerializer
    queryset = duelEnrollmentSchool.objects.all()

# Create your views here.
