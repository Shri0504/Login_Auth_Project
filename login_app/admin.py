from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_email_verified')
    # Filters to use in the admin panel
    list_filter = ('is_staff', 'is_active', 'is_email_verified', 'date_joined')
    # Fields to search for in the admin panel
    search_fields = ('username', 'email', 'first_name', 'last_name')
    # Ordering for the list view
    ordering = ('date_joined',)
    # Customizing the fieldsets (form layout in admin)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom Fields', {'fields': ('is_email_verified',)}),  # Add the custom field here
    )
    # Customizing fields for creating a user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'is_email_verified'),
        }),
    )

# Register the CustomUser model with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)
