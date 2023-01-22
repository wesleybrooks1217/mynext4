from rest_framework import serializers
from .models import CareerSurveyOne

class CareerSurveyOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSurveyOne
        fields = (
            'id',
            'question'
        )