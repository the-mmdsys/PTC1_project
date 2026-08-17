from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')), 
    path('ckeditor/', include('ckeditor_uploader.urls')), 
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), 
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), 
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('api/portfolio/', include('portfolio.api.urls')),
    path('api/blog/', include('blog.api.urls')),
    path('api/crm/', include('crm.api.urls')),
    path('api/about/', include('about.api.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns