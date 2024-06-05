from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='coordinator.username', read_only=True)
    email = serializers.CharField(source='coordinator.email', read_only=True)
    role = serializers.CharField(source='coordinator.role', read_only=True)
    class Meta:
        model = Event
        fields = ['id','coordinator','username', 'email','role', 'title', 'society_name', 'description', 'date','time', 'place', 'flex_image']
