from django.db import models

# Create your models here.

class Resources(models.Model):
    name = models.CharField(max_length=150)
    link = models.TextField()