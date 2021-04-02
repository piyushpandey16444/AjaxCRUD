from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'password']
    list_display_links = ['name', 'email', 'password']

# Register your models here.
