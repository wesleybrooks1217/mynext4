from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    public = models.BooleanField(default=True)
    year_est = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name

    # Add class / model functions here
    def years_since_est(self):
        return 2022 - self.year_est
