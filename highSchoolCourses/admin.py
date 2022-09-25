from django.contrib import admin
from .models import highSchoolCourses

class highSchoolCoursesAdmin(admin.ModelAdmin):
    list_display = (
    'courseName', 
    'AP',
    'courseScore',
    'english',
    'science',
    'socialStudies',
    'math',
    'humanity',
    'CTAE',
    'language',
    'fineArts',
    'health_PE',
    'preReqID')

# Register your models here.
admin.site.register(highSchoolCourses, highSchoolCoursesAdmin)