from books.views import BookListAndPostViews, BookUpdateAndDestroyViews

from django.urls import path

urlpatterns = [
    path("books/", BookListAndPostViews.as_view()),
    path("books/<str:book_id>/", BookUpdateAndDestroyViews.as_view()),
]
