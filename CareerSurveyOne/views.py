from django.shortcuts import render
from rest_framework import viewsets
from .models import CareerSurveyOne
from .serializers import CareerSurveyOneSerializer
from .forms import CareerSurveyOneForm
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
# Create your views here.

class CareerSurveyOneView(CreateAPIView, UpdateAPIView):
    queryset = CareerSurveyOne.objects.all()
    serializer_class = CareerSurveyOneSerializer
    form_class = CareerSurveyOneForm

    @action(detail=True, methods=['post'])
    def submit_survey(self, request, pk=None):
        survey = self.get_object()
        form = CareerSurveyOneForm(request.data, instance=survey)
        if form.is_valid():
            form.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
