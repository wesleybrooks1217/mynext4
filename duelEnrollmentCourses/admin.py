from django.contrib import admin
from .models import duelEnrollmentCourses, duelEnrollmentSchool

class duelEnrollmentCoursesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'courseScore',
        'preReqID'
    )

class duelEnrollmentSchoolAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address'
    )


admin.site.register(duelEnrollmentCourses, duelEnrollmentCoursesAdmin)
admin.site.register(duelEnrollmentSchool, duelEnrollmentSchoolAdmin)

# Register your models here.
