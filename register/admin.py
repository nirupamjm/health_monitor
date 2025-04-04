from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff']

# Debugging: Check if the model is being registered
print("Registering CustomUser model in admin...")

admin.site.register(CustomUser, CustomUserAdmin)
