from django.contrib import admin
from .models import School

class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'DEallowed',
        'schoolAddress',
        
    )

admin.site.register(School, SchoolAdmin)

# Register your models here.
