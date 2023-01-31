from django.db import models
from django.conf import settings
from CareerSurveyOne.models import Question

# Create your models here.
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

class CareerSurveyOneAnswers(models.Model):
    questionID = models.CharField(max_length=100, default='')
    userID = models.IntegerField(default=0)
    answer = models.CharField(max_length=100, default='')
   
   
   
   
   
   
   
   
   

