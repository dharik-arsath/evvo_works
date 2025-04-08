from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User  # Import your custom user model

class CustomUserAdmin(UserAdmin):
    # Remove references to 'username' since it doesn't exist in your model
    list_display = ('email', 'first_name', 'last_name', 'is_staff')  # Customize displayed fields
    ordering = ('email',)  # Use 'email' for ordering instead of 'username'
    search_fields = ('email', 'first_name', 'last_name')  # Customize search fields

    # Remove 'username' from fieldsets and add_form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

# Register your custom user model with the custom admin class
admin.site.register(User, CustomUserAdmin)