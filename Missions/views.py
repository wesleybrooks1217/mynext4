from django.shortcuts import render
from .models import Missions, userAccount
# Create your views here.

from rest_framework import viewsets

from .serializers import MissionSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Missions.objects.all()
    serializer_class = MissionSerializer

def assign_missions(request):
    users = userAccount.objects.all()
    for user in users:
        for i in range(1, 11):
            Missions.objects.create(user=user, title="Mission " + str(i), description="Description for Mission " + str(i), count=10, completed=False)
    return render(request, 'assigned.html')






