from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # If you have new fields, add them here
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('bio', 'location')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
