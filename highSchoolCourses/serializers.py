from rest_framework import serializers
from .models import highSchoolCourses


class highSchoolCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = highSchoolCourses
        fields = (
    'id',
    'courseName', 
    'AP',
    'courseScore',
    'english',
    'science',
    'socialStudies',
    'math',
    'humanity',
    'CTAE',
    'language',
    'fineArts',
    'health_PE',
    'preReqID')

