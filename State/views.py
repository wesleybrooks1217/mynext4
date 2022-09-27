from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StateSerializer
from .models import State

class StateView(viewsets.ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()

# Create your views here.
