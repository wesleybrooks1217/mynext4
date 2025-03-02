from rest_framework import serializers
from .models import Courses


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = (
    'id',
    'name',
    'ap',
    'duelEnrollment',
    'honors',
    'description',
    'difficulty',
    'units',
    'resources',
    'similar_classes')
