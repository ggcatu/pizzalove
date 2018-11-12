from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'pizza_love']

    fieldsets = UserAdmin.fieldsets + (('Love for pizza',  {'fields': ('pizza_love',)}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'pizza_love')}
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)