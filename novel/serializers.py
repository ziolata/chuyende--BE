from rest_framework import serializers
from .models import *
from django_filters import rest_framework as filters
from genres.serializers import *
from chapter.serializers import *
from genres.models import Author, Genres

class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = '__all__'
        # fields = ("id","name","image","genres","description","author","status","features","views","rating","numReviews","createdAt","updatedAt")

class NovelNewChapterSerializer(serializers.ModelSerializer):
    chapters = serializers.SerializerMethodField(read_only=True)
    genres = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Novel
        fields = '__all__'
    def get_chapters(self, obj):
        chapter = obj.chapter_set.order_by('-createdAt').first()
        if chapter:
            serializer = ChapterSerializer(chapter, many=False)
            return serializer.data
        return None  
    def get_genres(self, obj):
        genres = obj.genres.all()  # Lấy tất cả các thể loại của tiểu thuyết
        return [{'id': genre.id, 'name': genre.name} for genre in genres]

class NovelDetailSerializer(serializers.ModelSerializer):
    genres = GenresSerializer(many = True, read_only=True)
    author = serializers.SerializerMethodField(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    chapters = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Novel
        fields =  '__all__'
        extra_fields = ['author', 'reviews', 'chapters']
    
    def get_author(self, obj):
        author = obj.author
        serializer = AuthorSerializer(author, many=False)
        return serializer.data

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data

    def get_chapters(self, obj):
        chapters = obj.chapter_set.all()
        serializer = ChapterSerializer(chapters, many=True)
        return serializer.data
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
class GenresDetailSerializer(serializers.ModelSerializer):
    novels = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Genres
        fields = '__all__'
    def get_mangas(self, obj):
        novels = obj.novel_genres.all()
        serializer = NovelSerializer(novels, many=True)
        return serializer.data

class AuthorDetailSerializer(serializers.ModelSerializer):
    novels = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'

    def get_mangas(self, obj):
        novels = obj.novel_set.all()
        serializer = NovelSerializer(novels, many=True)
        return serializer.data