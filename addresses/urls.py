from django.urls import path
from . import views

urlpatterns = [
    path("adress/<pk>/", views.AdressDetail.as_view()),
]
