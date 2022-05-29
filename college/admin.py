from django.contrib import admin
from .models import College


class CollegeAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'public', 'year_est', 'description')

# Register your models here.

admin.site.register(College, CollegeAdmin)
