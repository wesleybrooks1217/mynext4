from rest_framework import serializers
from .models import School


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'id',
            'name',
            'stateID',
            'DEallowed',
            'schoolAddress',
            'englishUnits',
            'mathUnits',
            'scienceUnits',
            'socialStudiesUnits',
            'humanityUnits',
            'CTAEunits',
            'languageUnits',
            'fineArtsUnits',
            'CtaeLanguageFineArtsUnits',
            'healthPEUnits',
            'academicElectiveUnits',
            'freeElectiveUnits',
            'deSchools',
            'schoolCourses'
        )