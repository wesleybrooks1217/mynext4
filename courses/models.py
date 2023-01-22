
# Create your models here.
from django.db import models
from units.models import Units
from resources.models import Resources

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length=200, default="")
    ap = models.BooleanField(default=True)
    duelEnrollment = models.BooleanField(default=True)
    honors = models.BooleanField(default=True)
    description = models.TextField(default="")
    difficulty = models.IntegerField(default=0)
    units = models.ManyToManyField(Units)
    resources = models.ManyToManyField(Resources)
    similar_classes = models.ManyToManyField("self", blank=True)
    
    



    def __str__(self):
        return self.name