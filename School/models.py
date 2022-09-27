from django.db import models
from State.models import State
from duelEnrollmentCourses.models import duelEnrollmentSchool
from highSchoolCourses.models import highSchoolCourses


class School(models.Model):
    name = models.CharField(max_length = 175)
    stateID = models.ForeignKey(State, null = True, on_delete = models.SET_NULL)
    DEallowed = models.BooleanField()
    schoolAddress = models.CharField(max_length = 350)
    englishUnits = models.IntegerField()
    mathUnits = models.IntegerField()
    scienceUnits = models.IntegerField()
    socialStudiesUnits = models.IntegerField()
    humanityUnits = models.IntegerField()
    CTAEunits = models.IntegerField()
    languageUnits = models.IntegerField()
    fineArtsUnits = models.IntegerField()
    CtaeLanguageFineArtsUnits = models.IntegerField()
    healthPEUnits = models.IntegerField()
    academicElectiveUnits = models.IntegerField()
    freeElectiveUnits = models.IntegerField()
    deSchools = models.ManyToManyField(duelEnrollmentSchool)
    courses = models.ManyToManyField(highSchoolCourses)
    

# Create your models here.
