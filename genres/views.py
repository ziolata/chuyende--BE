from django.shortcuts import render
from rest_framework import generics, permissions, status, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import *
from novel.models import Novel
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from novel.serializers import GenresDetailSerializer, AuthorDetailSerializer,GenresSerializer, NovelSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_204_NO_CONTENT
# Create your views here.

class GenresListView(generics.ListAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

class SearchAdvance(generics.ListAPIView):
    permission_classes = [AllowAny]

    def list(self, request):
        try:
            query = request.query_params.getlist('keyword', '')

            # Capitalize each keyword for case-insensitive search
            for i in range(len(query)):
                query[i] = query[i].capitalize()

            # Filter novels by genres using case-insensitive search
            genres = Genres.objects.filter(name__in=query)
            novel_ids = genres.values_list('manga_genres', flat=True)  # Use 'manga_genres' as per your model
            novels = Novel.objects.filter(pk__in=novel_ids).order_by('-createdAt').distinct()

            serializer = NovelSerializer(novels, many=True)
            return Response({
                'novels': serializer.data
            })
        except Exception as e:
            return Response({'details': f"{e}"}, status=HTTP_204_NO_CONTENT)