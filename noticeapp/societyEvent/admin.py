from django.contrib import admin
from .models import Event

@admin.register(Event)
class Event(admin.ModelAdmin):
    list_display = ('title', 'society_name', 'date','time', 'place')
