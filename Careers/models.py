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

class States(models.Model):
    name = models.CharField(max_length=150)

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
    bullet_1 = models.CharField(max_length = 250, default = " ")
    bullet_2 = models.CharField(max_length = 250, default = " ")
    bullet_3 = models.CharField(max_length = 250, default = " ")
    bullet_4 = models.CharField(max_length = 250, default = " ")
    bullet_5 = models.CharField(max_length = 250, default = " ")
    what_they_do = models.TextField(default=" ")
    task_1 = models.TextField(default= " ")
    task_2 = models.TextField(default= " ")
    task_3 = models.TextField(default= " ")
    knowledge_1 = models.CharField(max_length=300, default=" ")
    knowledge_2 = models.CharField(max_length=300, default=" ")
    knowledge_3 = models.CharField(max_length=300, default= " ")
    knowledge_4 = models.CharField(max_length=300, default=" ")
    knowledge_5 = models.CharField(max_length=300, default=" ")
    knowledge_6 = models.CharField(max_length=300, default=" ")
    skills_1 = models.CharField(max_length=300, default=" ")
    skills_2 = models.CharField(max_length=300, default=" ")
    skills_3 = models.CharField(max_length=300, default=" ")
    skills_4 = models.CharField(max_length=300, default=" ")
    skills_5 = models.CharField(max_length=300, default=" ")
    abilities_1 = models.CharField(max_length=300, default=" ")
    abilities_2 = models.CharField(max_length=300, default=" ")
    abilities_3 = models.CharField(max_length=300, default=" ")
    abilities_4 = models.CharField(max_length=300, default=" ")
    abilities_5 = models.CharField(max_length=300, default=" ")
    abilities_6 = models.CharField(max_length=300, default=" ")
    abilities_7 = models.CharField(max_length=300, default = " ")
    char_1 = models.CharField(max_length=100, default=" ")
    char_2 = models.CharField(max_length=100, default=" ")
    char_3 = models.CharField(max_length=100, default=" ")
    char_4 = models.CharField(max_length=100, default=" ")
    char_5 = models.CharField(max_length=100, default=" ")
    char_6 = models.CharField(max_length=100, default=" ")
    tech_1 = models.CharField(max_length=100, default=" ")
    tech_2 = models.CharField(max_length=100, default=" ")
    tech_3 = models.CharField(max_length=100, default=" ")
    tech_4 = models.CharField(max_length=100, default=" ")
    tech_5 = models.CharField(max_length=100, default=" ")
    avg_degree = models.CharField(max_length=100, default=" ")
    annual_10th = models.IntegerField(default=0)
    annual_median = models.IntegerField(default=0)
    annual_90th = models.IntegerField(default=0)
    hourly_10th = models.IntegerField(default = 0)
    hourly_median = models.IntegerField(default = 0)
    hourly_90th = models.IntegerField(default=0)
    num_states_above = models.IntegerField(default=0)
    num_states_avg = models.IntegerField(default = 0)
    num_states_below = models.IntegerField(default=0)
    above_avg_states = models.ManyToManyField(States, blank=True)
    similar_careers = models.ManyToManyField("Career", blank=True)
    industry_1_name = models.CharField(max_length=300, default=" ")
    industry_1_percent = models.IntegerField(default=0)
    industry_2_name = models.CharField(max_length=300, default=" ")
    industry_2_percent = models.IntegerField(default=0)
    industry_3_name = models.CharField(max_length=300, default=0)
    industry_3_percent = models.IntegerField(default=0)




