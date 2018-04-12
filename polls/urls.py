from django.conf.urls import url
from welcome.views import index, health
from . import views

urlpatterns = [
	url(r'^$', index),
]