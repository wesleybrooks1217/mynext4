from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccomplishmentsSerializer, UserSerializer
from .models import Accomplishments, AbstractBaseUser
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny


class AccomplishmentsView(viewsets.ModelViewSet):
    serializer_class = AccomplishmentsSerializer
    queryset = Accomplishments.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny, )
        return super(UserViewSet, self).get_permissions()
    
    


# Create your views here.
