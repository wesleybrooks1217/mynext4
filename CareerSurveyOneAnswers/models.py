from django.db import models

# Create your models here.

class CareerSurveyOneAnswers(models.Model):
    questionID = models.IntegerField()
    userID = models.IntegerField()
    answer = models.IntegerField()