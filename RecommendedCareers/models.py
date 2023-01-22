from django.db import models

# Create your models here.

class RecommendedCareers(models.Model):
    userID = models.IntegerField()
    careerID = models.IntegerField()
    similarity = models.FloatField()
