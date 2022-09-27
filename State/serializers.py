from rest_framework import serializers
from .models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = (
            'id',
            'meritAID',
            'gpaAID',
            'satAID',
            'actAID',
            'freeCommunityCollege',
            'deAID',
            'deAIDyear',
            'deAIDgpa',
            'deAIDsat',
            'deAIDact',
            'techSchoolAID',
            'onlineCourseProgram',
            'onlineCourseAID',
            'onlineCourses'
        )