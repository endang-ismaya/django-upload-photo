from django.urls import path

from apps.feeds.views import HomePageView, PostDetailView, PostAddView

urlpatterns = [
    path("", HomePageView.as_view(), name="feeds__home"),
    path("details/<int:pk>/", PostDetailView.as_view(), name="feeds__detail"),
    path("posts/add/", PostAddView.as_view(), name="feeds__addpost"),
]
