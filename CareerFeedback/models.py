from django.db import models


# Create your models here.
class CareerFeedback(models.Model):
    userID = models.IntegerField()
    careerID = models.IntegerField()
    score = models.FloatField()