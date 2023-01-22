from django.db import models

# Create your models here.

class CareerSurveyOne(models.Model):
    question = models.TextField(default="")
    
