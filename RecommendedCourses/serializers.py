from rest_framework import serializers
from .models import RecommendedCourses


class RecommendedCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedCourses
        fields = (
            'id',
            'courseID',
            'userID',
            'similarityScore'
        )