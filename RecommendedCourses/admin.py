from django.contrib import admin
from .models import RecommendedCourses

# Register your models here.

class RecommendedCoursesAdmin(admin.ModelAdmin):
    list_display = (
        'courseID',
        'userID',
        'similarityScore'
    )


admin.site.register(RecommendedCourses, RecommendedCoursesAdmin)
