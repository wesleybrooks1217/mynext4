from django.contrib import admin
from .models import College


class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'collegeAIKey')

# Register your models here.

admin.site.register(College, CollegeAdmin)
