from django.contrib import admin
from .models import Resources

# Register your models here.
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("name", "link")

admin.site.register(Resources, ResourceAdmin)