from django.db import models

class State(models.Model):
    YEAR = (
        (9, '9th'),
        (10, '10th'),
        (11, '11th'),
        (12, '12th')
    )
    meritAID = models.BooleanField()
    gpaAID = models.FloatField(blank = True)
    satAID = models.IntegerField(blank = True)
    actAID = models.IntegerField(blank = True)
    freeCommunityCollege = models.BooleanField()
    deAID = models.BooleanField()
    deAIDyear = models.IntegerField(default = 11, choices = YEAR) 
    deAIDgpa = models.FloatField(blank = True)
    deAIDsat = models.IntegerField(blank = True)
    deAIDact = models.IntegerField(blank = True)
    techSchoolAID = models.BooleanField()
    onlineCourseProgram = models.BooleanField()
    onlineCourseAID = models.BooleanField()
    