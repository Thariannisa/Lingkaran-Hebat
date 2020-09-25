from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, EditView, Success

app_name = "core"
urlpatterns = [
    path('', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('edit/<int:pk>', EditView.as_view(), name="update"),
    path('success/<int:pk>', Success, name="success"),
]
