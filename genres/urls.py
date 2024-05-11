from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views
app_name = 'genres'

urlpatterns = [
    path('search/', views.SearchAdvance.as_view(), name='Search Advance'),
    path('list/', views.GenresListView.as_view(), name='List Genres'),
    
   
]

