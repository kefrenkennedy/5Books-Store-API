from django.urls import path
from reviews.views import (
    ReviewListAndCreateViews,
    ReviewRetriveUpdateDestroyViews
)


urlpatterns = [
    path("reviews/", ReviewListAndCreateViews.as_view()),
    path(
        "reviews/<str:review_id>/",
        ReviewRetriveUpdateDestroyViews.as_view()
    ),
]
