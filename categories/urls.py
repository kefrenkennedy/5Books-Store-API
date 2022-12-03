from categories.views import CategoriesListAndCreateViews, CategoriesPatchDestroyViews

from django.urls import path

urlpatterns = [
    path("categories/", CategoriesListAndCreateViews.as_view()),
    path("categories/<pk>/", CategoriesPatchDestroyViews.as_view()),
]
