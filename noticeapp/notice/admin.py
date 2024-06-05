from django.contrib import admin
from .models import Document

@admin.register(Document)
class Document(admin.ModelAdmin):
    list_display = ( 'file_title', 'id')
