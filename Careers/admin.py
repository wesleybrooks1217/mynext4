from django.contrib import admin
from .models import Skills, Industry, Career, States
# Register your models here.

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class IndustryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class CareerAdmin(admin.ModelAdmin):
    list_display = (
    'name',
    'dailyTasks',
    'description',
    'futureOutlook',
    'requiresCollege',
    'requiresGradSchool')

class StateAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

admin.site.register(Skills, SkillsAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(States, StateAdmin)