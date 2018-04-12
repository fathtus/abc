from django.conf.urls import url
from polls.views import index, health
from . import views

urlpatterns = [
	url(r'^$', index),
]