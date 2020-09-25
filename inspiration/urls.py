from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import ListInspiration, DetailInspiration, Likes, Claps
from django.views.generic import TemplateView

app_name = "inspiration"

urlpatterns = [
    path("", ListInspiration.as_view(), name="list"),
    path("detail/<int:pk>", DetailInspiration.as_view(), name="detail"),
    path("like/<int:pk>", Likes, name='like'),
    path("clap/<int:pk>", Claps, name='clap'),
]
