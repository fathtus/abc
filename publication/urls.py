from django.urls import path
from .views import PublisherList

urlpatterns = [
    path('publishers/', PublisherList.as_view()),
]