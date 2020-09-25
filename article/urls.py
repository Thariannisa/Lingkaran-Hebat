from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import ListArticle, DetailArticle, Likees, Clapes
from django.views.generic import TemplateView

app_name = "article"

urlpatterns = [
    path("", ListArticle.as_view(), name="list"),
    path("detail/<int:pk>", DetailArticle.as_view(), name="detail"),
    path("like/<int:pk>", Likees, name='like'),
    path("clap/<int:pk>", Clapes, name='clap'),
]
