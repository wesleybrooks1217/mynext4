from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SchoolSerializer
from .models import School

class SchoolView(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

# Create your views here.
