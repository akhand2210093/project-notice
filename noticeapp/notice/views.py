from rest_framework import status, views
from rest_framework.response import Response
from .models import Document
from .serializers import DocumentSerializer
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

class DocumentGetAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

class DocumentGetDetailAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        document = self.get_object(pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

class DocumentPostAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        if request.user.role == 'staff' or request.user.role == 'administrator':
            request.data['editor'] = request.user.id
            serializer = DocumentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg':'user do not have permission.'}, status=status.HTTP_400_BAD_REQUEST)
    
class DocumentUpdateAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self, pk):
        try:
            return Document.objects.get(pk=pk)
        except Document.DoesNotExist:
            raise Http404
        
    def put(self, request, pk):
        if request.user.role == 'staff' or request.user.role == 'administrator':
            document = self.get_object(pk)
            request.data['editor'] = request.user.id
            serializer = DocumentSerializer(document, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg':'user do not have permission.'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        if request.user.role == 'staff' or request.user.role == 'administrator':
            document = self.get_object(pk)
            document.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'msg':'user do not have permission.'}, status=status.HTTP_400_BAD_REQUEST)
    