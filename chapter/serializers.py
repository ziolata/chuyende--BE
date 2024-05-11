from rest_framework import serializers
from .models import Chapter, ChapterContent

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'
        
class ChapterContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterContent
        fields = '__all__'

class ChapterDetailSerializer(serializers.ModelSerializer):
    chapterContent = serializers.SerializerMethodField(read_only=True)
    novelname = serializers.ReadOnlyField(source='novel.name')
    class Meta:
        model = Chapter
        fields = '__all__'

    def get_chapterContent(self, obj):
        content = obj.chaptercontent_set.first() 
        serializer = ChapterContentSerializer(content)
        return serializer.data