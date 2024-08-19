from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('siteapi/posts/', include('posts.urls')),
    path('siteapi/comment/', include('comment.urls')),
    path('siteapi/sort/', include('sort.urls')),
    path('siteapi/user/', include('user.urls')),
    path('admin/', admin.site.urls),
    # path('ckeditor/', include('ckeditor_uploader.urls')),


    # Swagger UI:
    path('doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc UI:
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# ADMIN PANEL CUSTOMIZATION
admin.site.site_title = "پنل ادمین"
admin.site.site_header = "پنل ادمین بلاگ"
admin.site.index_title = "پنل ادمین بلاگ"