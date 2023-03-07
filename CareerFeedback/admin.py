from django.contrib import admin
from .models import CareerFeedback
# Register your models here.
class CareerFeedbackAdmin(admin.ModelAdmin):
    list_display = (
        'score',
        'id'
    )

admin.site.register(CareerFeedback, CareerFeedbackAdmin)