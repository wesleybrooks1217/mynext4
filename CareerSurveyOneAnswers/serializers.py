from rest_framework import serializers
from .models import CareerSurveyOneAnswers

class CareerSurveyOneAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSurveyOneAnswers
        fields = ['survey_id', 'user_id', 'answer']
        