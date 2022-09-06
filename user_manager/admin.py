import email
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserManager

# Register your models here.
class CustomUserManager(UserAdmin):
    readonly_fields=('updated_at',)

    fieldsets = (
        ("Credentials", {"fields": ("username", "password")}),
        ("User Info", {"fields": ("first_name","last_name","birthdate", "email", "is_critic","bio", "updated_at")}),
    )

    

admin.site.register(UserManager, CustomUserManager)
