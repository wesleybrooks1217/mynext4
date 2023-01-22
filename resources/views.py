from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ResourceSerializer
from .models import Resources

class ResourceView(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    queryset = Resources.objects.all()

# Create your views here.
