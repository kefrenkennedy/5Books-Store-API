from django.urls import path
from .views import ListCreateUserView, LoginView, UpdateActiveView, UpdateUserView
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("users/", ListCreateUserView.as_view()),
    path("users/<pk>/management", UpdateActiveView.as_view()),
    path("login/", obtain_auth_token),
    path("users/<pk>", UpdateUserView.as_view()),
]
