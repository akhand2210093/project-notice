from django.contrib import admin
from .models import User

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'year', 'is_staff')
    list_filter = ( 'email', 'year', 'branch', 'role')
    search_fields = ( 'email','username', 'branch')

    
