from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('root/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='blog:post-list', permanent=False), name='index'),
    path('blog/', include('blog.urls', namespace='blog'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
