from django.views.generic import TemplateView, DetailView

from apps.feeds.models import Post


class HomePageView(TemplateView):
    template_name = "feeds/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()

        return context


class PostDetailView(DetailView):
    template_name = "feeds/detail.html"
    model = Post
