from django.urls import path

from . import views

urlpatterns = [
    path('authors/', views.AuthorView.as_view()),
    path('authors/<pk>/', views.DetailAuthorView.as_view())

]