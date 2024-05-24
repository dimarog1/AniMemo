from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from AniMemo import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('anime.urls')),
    path('users/', include('users.urls')),
    # path('auth/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
