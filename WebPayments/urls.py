from django.urls import path
from django.urls.resolvers import URLPattern
from .views import base, index
from django.urls import path

urlpatterns = [
    path("index/", index, name="index")
]
