from operator import mod
from django.db import models

# Create your models here.

class Skills(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()


class Industry(models.Model):
    name = models.CharField(max_length = 120)
    icon = models.ImageField()
    description = models.TextField()
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return self.name

class Career(models.Model):
    industryID = models.ForeignKey(Industry, null = True, on_delete = models.SET_NULL)
    name = models.CharField(max_length = 100)
    dailyTasks = models.TextField()
    description = models.TextField()
    futureOutlook = models.FloatField()
    requiresCollege = models.BooleanField()
    requiresGradSchool = models.BooleanField()
    majorID = models.IntegerField()
    skills = models.ManyToManyField(Skills)


