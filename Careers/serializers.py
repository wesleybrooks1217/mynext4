from rest_framework import serializers
from .models import Skills, Industry, Career

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = (
            "id",
            'name',
            "description"
            )

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = (
            "id",
            "name",
            "icon",
            "description",
            "skills"
        )

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = (
            "id",
            "industryID",
            "name",
            "dailyTasks",
            "description",
            "futureOutlook",
            "requiresCollege",
            "requiresGradSchool",
            "majorID",
            "skills"
        )