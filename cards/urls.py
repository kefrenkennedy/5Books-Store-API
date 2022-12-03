from django.urls import path
from cards.views import CardGetPostViews, CardUpdateDeleteViews


urlpatterns = [
    path("credit_card/", CardGetPostViews.as_view()),
    path("credit_card/<pk>", CardUpdateDeleteViews.as_view()),
]
