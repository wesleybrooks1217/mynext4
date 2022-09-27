from dataclasses import field
from rest_framework import serializers
from .models import duelEnrollmentCourses, duelEnrollmentSchool

class duelEnrollmentCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = duelEnrollmentCourses
        fields = (
            'id',
            'name',
            'courseScore',
            'preReqID',
            'english',
            'science',
            'socialStudies',
            'math',
            'humanity',
            'language',
            'fineArts',
            'earlyChildhood',
            'cyberSecurity',
            'digitalMedia',
            'it',
            'emt',
            'healtTech',
            'nursing',
            'carpentry',
            'hvac',
            'machining',
            'weilding'
        )

class duelEnrollmentSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = duelEnrollmentSchool
        fields = (
            'id',
            'name',
            'address',
            'courses'
        )