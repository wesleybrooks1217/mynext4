from django.db import models
from userAccount.models import userAccount
from courses.models import Courses

class RecommendedCourses(models.Model):

    courseID = models.ForeignKey(Courses, related_name="CourseID", null = True, on_delete = models.SET_NULL)
    userID = models.ForeignKey(userAccount, related_name = "UserID", null = True, on_delete = models.SET_NULL)
    similarityScore = models.FloatField(null = True)
    
