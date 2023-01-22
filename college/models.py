from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=120)
    collegeAIKey = models.IntegerField(null = True)

    def __str__(self):
        return self.name

