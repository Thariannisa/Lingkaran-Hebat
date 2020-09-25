from django.contrib import admin
from django.urls import path
from django.conf import settings
from .views import CreateRiwayat, ListRiwayat, UpdateRiwayat

app_name = "riwayat"

urlpatterns = [
    path('create', CreateRiwayat.as_view(), name='create'),
    path("", ListRiwayat.as_view(), name="list"),
    path("update/<int:pk>", UpdateRiwayat.as_view(), name="update"),
]
