from django.contrib import admin
from .models import Courses

class highSchoolCoursesAdmin(admin.ModelAdmin):
    list_display = (
    'name',
    'ap',
    'duelEnrollment',
    'honors',
    'description',
    'difficulty')

# Register your models here.
admin.site.register(Courses, highSchoolCoursesAdmin)