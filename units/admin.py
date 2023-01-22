from django.contrib import admin
from .models import Units

# Register your models here.

class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "description")

admin.site.register(Units, UnitAdmin)