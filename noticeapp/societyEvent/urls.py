from django.urls import path
from .views import EventGetAll, EventPost,EventGetApi, EventUpdateApi

urlpatterns = [
    path('eventAll/', EventGetAll.as_view(), name='document-list-create'),
    path('eventPost/', EventPost.as_view(), name='document-list-create'),
    path('event/<int:pk>/', EventGetApi.as_view(), name='flex-detail'),
    path('eventUpdate/<int:pk>/', EventUpdateApi.as_view(), name='flex-detail'),
]
