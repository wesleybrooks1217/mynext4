from rest_framework import serializers
from .models import CareerSurveyOne

class CareerSurveyOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = CareerSurveyOne
        fields = ('secondary_school', 
        'tertiary_school', 
        'independent_school', 
        'work_from_home', 
        'favorite_subject', 
        'favorite_careers', 
        'shifting_schedule', 
        'socializing_more',
        'sports_as_career',
        'travel_for_work'
        )
