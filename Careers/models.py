from operator import mod
from django.db import models

# Create your models here.



class Career(models.Model):
    
    name = models.CharField(max_length=200, default="")
    onetID = models.CharField(max_length=200, default="")
    



