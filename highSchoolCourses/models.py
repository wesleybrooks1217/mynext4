from django.db import models

# Create your models here.
class highSchoolCourses(models.Model):
    courseName = models.CharField(max_length = 75)
    AP = models.BooleanField(default = False)
    courseScore = models.FloatField()
    english = models.BooleanField(default = False)
    science = models.BooleanField(default = False)
    socialStudies = models.BooleanField(default = False)
    math = models.BooleanField(default = False)
    humanity = models.BooleanField(default = False)
    CTAE = models.BooleanField(default = False)
    language = models.BooleanField(default = False)
    fineArts = models.BooleanField(default = False)
    health_PE = models.BooleanField(default = False)
    preReqID = models.IntegerField(null=True, blank = True)
    desciption = models.TextField(default = " ")
    difficulty = models.FloatField(default = 0)
    



    def __str__(self):
        return self.courseName
