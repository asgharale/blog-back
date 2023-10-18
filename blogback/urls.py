from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('siteapi/posts/', include('posts.urls')),
    path('siteapi/comment/', include('comment.urls')),
    path('siteapi/sort/', include('sort.urls')),
    path('siteapi/user/', include('user.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
