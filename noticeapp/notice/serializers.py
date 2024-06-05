from rest_framework import serializers
from .models import Document

class DocumentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='editor.username', read_only=True)
    email = serializers.CharField(source='editor.email', read_only=True)
    role = serializers.CharField(source='editor.role', read_only=True)
    class Meta:
        model = Document
        fields = ('id','editor','username', 'email','role','file_title','pdf','uploaded_at')