from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "id",
        "email",
        "username",
        "name",
        "profile_img",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("name", "profile_img",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields" : ("name", "profile_img",)}),)

admin.site.register(CustomUser, CustomUserAdmin)