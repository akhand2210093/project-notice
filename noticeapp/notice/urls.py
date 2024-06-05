from django.urls import path
from .views import DocumentGetAPIView, DocumentPostAPIView, DocumentGetDetailAPIView, DocumentUpdateAPIView


urlpatterns = [
    path('docAll/', DocumentGetAPIView.as_view(), name='document-list-create'),
    path('docPost/', DocumentPostAPIView.as_view(), name='document-list-create'),
    path('docGet/<int:pk>/', DocumentGetDetailAPIView.as_view(), name='document-detail'),
    path('docUpdate/<int:pk>/', DocumentUpdateAPIView.as_view(), name='document-detail'),
]
