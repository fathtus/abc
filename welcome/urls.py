from django.conf.urls import url
from polls.views import index
from django.urls import path

from . import views


app_name = 'welcome'
urlpatterns = [
    path('', views.index, name='index'),
    path('calculate', views.calculate, name='calculate'),
    path('get-name', views.get_name, name='get_name'),
    path('contact', views.contact, name='contact'),
    path('author', views.authorForm, name='authorForm'),
]
