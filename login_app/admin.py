
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'mobile_no', 'is_email_verified', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('mobile_no', 'is_email_verified')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('mobile_no', 'is_email_verified')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
