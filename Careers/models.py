from operator import mod
from django.db import models
from courses import models as CoursesMod
from college import models as CollegeMod

# Create your models here.



class Career(models.Model):
    
    name = models.CharField(max_length=200, default="")
    onetID = models.CharField(max_length=200, default="")
    median_salary = models.IntegerField(default=0)
    industry = models.CharField(max_length=200, default="")
    useful_courses = models.ManyToManyField(CoursesMod.Courses, verbose_name=_("courses"))
    popular_colleges = models.ManyToManyField(CollegeMod.College, verbose_name=_("colleges"))
    