import rest_framework
from core_app_root.ai_applications.serializers.booksummarizer import BookSummarizerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
class BookSummarizerViewset(viewsets.ModelViewSet):
    serializer_class=BookSummarizerSerializer
    def create(request):
        serializer=BookSummarizerSerializer(data=request.data)

        if serializer.is_valid():
            print(serializer)
            return Response({"message":"good"},status=status.HTTP_200_OK)

