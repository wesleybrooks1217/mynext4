from django.db import models

# Create your models here.
class CareerFeedback(models.Model):
    userID = models.IntegerField(blank=True, default=0)
    careerID = models.IntegerField(blank=True, default=0)
    score = models.FloatField(blank=True, default=0.0)