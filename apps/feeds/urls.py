from django.urls import path

from apps.feeds.views import HomePageView, PostDetailView

urlpatterns = [
    path("", HomePageView.as_view(), name="feeds__home"),
    path("details/<int:pk>/", PostDetailView.as_view(), name="feeds__detail"),
]
