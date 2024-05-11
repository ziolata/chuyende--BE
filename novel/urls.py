from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
app_name = 'novel'

urlpatterns = [
    path('list/', views.NovelList.as_view(), name='Novel List'),
    path('list/newupdate/', views.NewUpdateNovelView.as_view(), name='Novel New Update List'),
    path('list/hot/', views.HotNovelView.as_view(), name='Hot Novel List'),
    path('list/topnovel/', views.TopNovelView.as_view(), name='Novel Top'),
    path('list/<int:pk>/', views.NovelDetailView.as_view(), name='Novel List'),
    path('review/', views.NovelCreateReview.as_view(), name='Novel List'),
   
]

