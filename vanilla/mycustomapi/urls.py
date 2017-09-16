from django.conf.urls import include, url
from django.contrib import admin
from oscar.app import application as oscar

from .app import application as api


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api.urls)),
    url(r'', include(oscar.urls)),

]
