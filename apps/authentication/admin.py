from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ('email', 'phone_number', 'is_staff')
    list_filter = ('email', 'phone_number', 'manager')
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password', 'manager')}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        ('Permissions', {'fields': ('user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password1', 'password2', 'manager'),
        }),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        ('Permissions', {'fields': ('user_permissions',)}),
    )


admin.site.register(User, UserAdmin)
