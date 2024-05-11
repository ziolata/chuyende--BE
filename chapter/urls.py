from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
app_name = 'chapter'

urlpatterns = [
    path('<int:pk>/', views.ChapterDetailView.as_view(), name='Chapter Detail'),
    path('content/<int:pk>/', views.ChapterContentView.as_view(), name='Chapter Detail'),
    path('list/', views.ChapterView.as_view(), name='Chapter Detail'),
    
    path('by/<int:pk>/', views.ChapterView.as_view(), name="chapters-novel"),
    
]

