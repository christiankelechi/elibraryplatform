from rest_framework import serializers
from core_app_root.ai_applications.models import TextModel
class BookSummarizerSerializer(serializers.Serializer):
    class Meta:
        model=TextModel
        