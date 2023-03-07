from django.db import models
from userAccount.models import userAccount
# Create your models here.


class Missions(models.Model):
    userID = models.ForeignKey(userAccount, related_name = "missions_set", null = True, on_delete = models.SET_NULL)
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='missions/')
    count = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)
   
   
   
   
   
   