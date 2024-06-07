from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from .models import Event
from .serializers import EventSerializer

class EventGetAll(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        event_objects = Event.objects.all()
        serializer = EventSerializer(event_objects, many=True)
        return Response(serializer.data)

class EventPost(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.user.role == 'staff' or request.user.role == 'administrator':
            request.data['coordinator'] = request.user.id
            serializer = EventSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg':'Student user do not have permission.'}, status=status.HTTP_400_BAD_REQUEST)
        

class EventGetApi(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)

    def get(self, request, pk):
        flex_object = self.get_object(pk)
        serializer = EventSerializer(flex_object)
        return Response(serializer.data)

class EventUpdateApi(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(Event, pk=pk)
    
    def put(self, request, pk):
        if request.user.role == 'staff' or request.user.role == 'administrator':
            flex_object = self.get_object(pk)
            if request.user.username == flex_object.coordinator.username :
                serializer = EventSerializer(flex_object, data=request.data, partial = True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'msg':'Access denied'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg':'Student user do not have permission.'}, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self, request, pk):
        if request.user.role == 'staff' or request.user.role == 'administrator':
            flex_object = self.get_object(pk)
            if request.user.username == flex_object.coordinator.username :
                flex_object.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'msg':'Access denied'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg':'Student user do not have permission.'}, status=status.HTTP_400_BAD_REQUEST)