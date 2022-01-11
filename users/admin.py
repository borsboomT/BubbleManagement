from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.forms import CheckboxSelectMultiple

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    list_display = ('email','first_name','last_name', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name','entryNodes')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser,CustomUserAdmin)