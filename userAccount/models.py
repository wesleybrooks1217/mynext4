from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from School.models import School
from Careers.models import Career
from college.models import College
from courses.models import Courses

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
    
    def simulat_user_create(email, username, password):
       user, _ =  userAccount.objects.get_or_create(
           email = email,
           username = username,
           password = password
       )

       return user.id

       
            

        

        
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
    school = models.ForeignKey(School, null = True, on_delete = models.SET_NULL, blank=True)
    #password = models.CharField(max_length = 30)
    firstName = models.CharField(max_length = 35, blank=True)
    lastName = models.CharField(max_length = 35, blank=True)
    YEAR = (
        (9, '9th'),
        (10, '10th'),
        (11, '11th'),
        (12, '12th')
    )
    year = models.IntegerField(default = 9, choices = YEAR)
    wantsCollege = models.BooleanField(null = True, blank=True)
    gpa = models.FloatField(null = True, blank=True)
    numHonorsClasses = models.IntegerField(null = True, blank=True)
    numAPClasses = models.IntegerField(null = True, blank=True)
    numIBClasses = models.IntegerField(null = True, blank=True)
    numDEClasses = models.IntegerField(null = True, blank=True)
    familyIncome = models.IntegerField(null = True, blank=True)
    maxSpending = models.IntegerField(null = True, blank=True)
    sat = models.IntegerField(null = True, blank=True)
    satAttempts = models.IntegerField(null = True, blank=True)
    act = models.IntegerField(null = True, blank=True)

    accomplishments = models.ManyToManyField(Accomplishments, blank=True)

    likedSchools = models.ManyToManyField(College, related_name="LikedColleges", blank=True)
    dislikedSchools = models.ManyToManyField(College, related_name="DislikedColleges", blank=True)
    favoriteSchool = models.ForeignKey(College, related_name = 'favoriteSchool', null = True, on_delete = models.SET_NULL, blank=True)
    
    likedCareers = models.ManyToManyField(Career, related_name = 'likedCareers', blank=True)
    dislikedCareers = models.ManyToManyField(Career, related_name= 'dislikedCareers', blank=True)
    favCareer = models.ForeignKey(Career, related_name = 'favCareer', null = True, on_delete = models.SET_NULL, blank=True)

    likedCourses = models.ManyToManyField(Courses, related_name = 'likedCourses', blank=True)
    dislikedCourses = models.ManyToManyField(Courses, related_name= 'dislikedCourses', blank=True)
    
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    
    def get_id(self):
        return self.get_id()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

    
    #Given a users SAT score, find what 
    #percentile their score is in
    def sat_percentile(self):
        return 0

    
    #Given a users ACT score, find what
    #percentile their score is in
    def act_percentile(self):
        return 0


    #Given a users #AP, #DE, and #IB
    #return how many rigours classes they have
    #taken
    def course_rigor_number(self):
        return 0


    #given how many rigours classes a user has taken
    #return how their rigor score compares to the rest
    #of the country

    def course_rigor_percentile(self):
        return 0




# Create your models here.
