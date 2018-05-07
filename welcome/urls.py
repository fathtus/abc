from django.conf.urls import url
from polls.views import index
from django.urls import path

from . import views

app_name = 'welcome'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('calculate', views.calculate, name='calculate'),
]
