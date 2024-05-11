
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('Auth.urls')),
    path('api/novel/', include('novel.urls')),
    path('api/chapter/', include('chapter.urls')),
    path('api/genres/', include('genres.urls')),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)