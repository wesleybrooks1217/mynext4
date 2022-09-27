from operator import mod
from django.db import models

# Create your models here.

class duelEnrollmentCourses(models.Model):
    name = models.CharField(max_length = 50)
    courseScore = models.FloatField()
    preReqID = models.IntegerField(blank = True)
    english = models.BooleanField()
    science = models.BooleanField()
    socialStudies = models.BooleanField()
    math = models.BooleanField()
    humanity = models.BooleanField()
    language = models.BooleanField()
    fineArts = models.BooleanField()
    earlyChildhood = models.BooleanField()
    cyberSecurity = models.BooleanField()
    digitalMedia = models.BooleanField()
    it = models.BooleanField()
    emt = models.BooleanField()
    healthTech = models.BooleanField()
    nursing = models.BooleanField()
    carpentry = models.BooleanField()
    electrician = models.BooleanField()
    hvac = models.BooleanField()
    machining = models.BooleanField()
    weilding = models.BooleanField()


class duelEnrollmentSchool(models.Model):
    name = models.CharField(max_length = 75)
    address = models.CharField(max_length = 200)
    courses = models.ManyToManyField(duelEnrollmentCourses)
