from django.contrib import admin
from .models import State

class StateAdmin(admin.ModelAdmin):
    list_display = (
        'meritAID',
        'gpaAID',
        'freeCommunityCollege',
        'deAID',
        'techSchoolAID',
        'onlineCourseProgram',
        'onlineCourseAID'
    )

admin.site.register(State, StateAdmin)

# Register your models here.
