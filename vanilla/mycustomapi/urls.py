from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application as oscar
from django.conf import settings
from django.conf.urls.static import static

from .app import application as api


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api.urls)),
    url(r'', include(oscar.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
