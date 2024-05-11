from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
 
from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import UserCustom
from . import models
 
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserCustom
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
 
 
admin.site.register(UserCustom, CustomUserAdmin)

@admin.register(models.Role)
class Role(admin.ModelAdmin):
    list_display = ('name',)
