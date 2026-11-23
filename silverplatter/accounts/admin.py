from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Adds the `role` field to the normal Django user admin page."""
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('role',)
    fieldsets = UserAdmin.fieldsets + (
        ('Silver Platter role', {'fields': ('role', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Silver Platter role', {'fields': ('role', 'phone', 'email')}),
    )
