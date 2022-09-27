from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccomplishmentsSerializer, UserSerializer
from .models import Accomplishments, AbstractBaseUser

class AccomplishmentsView(viewsets.ModelViewSet):
    serializer_class = AccomplishmentsSerializer
    queryset = Accomplishments.objects.all()



# Create your views here.
