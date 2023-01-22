from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UnitSerializer
from .models import Units

class UnitView(viewsets.ModelViewSet):
    serializer_class = UnitSerializer
    queryset = Units.objects.all()

# Create your views here.
