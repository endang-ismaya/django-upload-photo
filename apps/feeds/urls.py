from django.urls import path

from apps.feeds.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
]
