from django.conf import settings
from django.conf.urls import include, url

from welcome.views import index, health

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    url(r'^$', index),
    url(r'^health$', health),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('welcome/', include('welcome.urls')),
    path('publication/', include('publication.urls')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
