from django.contrib import admin
from .models import Accomplishments, userAccount, MyAccountManager


class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        
    )
admin.site.register(Accomplishments)
admin.site.register(userAccount, UserAccountAdmin)



# Register your models here.
