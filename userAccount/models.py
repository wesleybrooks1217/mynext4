from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from School.models import School
from Careers.models import Industry, Career
from highSchoolCourses.models import highSchoolCourses
from college.models import College

class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Accomplishments(models.Model):
    name = models.CharField(max_length = 50)
    leadership = models.BooleanField()
    schoolAward = models.BooleanField()
    stateAward = models.BooleanField()
    nationalAward = models.BooleanField()
    competition = models.BooleanField()

class userAccount(AbstractBaseUser):
    email = models.EmailField( max_length = 60, unique = True)
    username = models.CharField(max_length = 30, unique = True)
    date_joined = models.DateTimeField( auto_now_add = True)
    last_login = models.DateTimeField( auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    school = models.ForeignKey(School, null = True, on_delete = models.SET_NULL)
    #password = models.CharField(max_length = 30)
    firstName = models.CharField(max_length = 35)
    lastName = models.CharField(max_length = 35)
    YEAR = (
        (9, '9th'),
        (10, '10th'),
        (11, '11th'),
        (12, '12th')
    )
    year = models.IntegerField(default = 9, choices = YEAR)
    desiredIndustry = models.ForeignKey(Industry, null = True, on_delete = models.SET_NULL)
    wantsCollege = models.BooleanField(null = True)
    gpa = models.FloatField(null = True)
    numHonorsClasses = models.IntegerField(null = True)
    numAPClasses = models.IntegerField(null = True)
    numIBClasses = models.IntegerField(null = True)
    numDEClasses = models.IntegerField(null = True)
    familyIncome = models.IntegerField(null = True)
    maxSpending = models.IntegerField(null = True)
    sat = models.IntegerField(null = True)
    satAttempts = models.IntegerField(null = True)
    act = models.IntegerField(null = True)
    accomplishments = models.ManyToManyField(Accomplishments)
    prevCourses = models.ManyToManyField(highSchoolCourses)
    likedSchools = models.ManyToManyField(College)
    #recommendedCourses = models.ManyToManyField(highSchoolCourses)
    likedCareers = models.ManyToManyField(Career)
    #recommendedCareers = models.ManyToManyField(Career)
    #likedCourses = models.ManyToManyField(highSchoolCourses)
    #dislikedCourses = models.ManyToManyField(highSchoolCourses)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True



    




# Create your models here.
