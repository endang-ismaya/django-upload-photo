from django.views.generic import TemplateView, DetailView, FormView
from django.urls import reverse_lazy

from apps.feeds.forms import PostForm
from apps.feeds.models import Post


class HomePageView(TemplateView):
    template_name = "feeds/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by("-created_at")

        return context


class PostDetailView(DetailView):
    template_name = "feeds/detail.html"
    model = Post


class PostAddView(FormView):
    template_name = "feeds/post-add.html"
    form_class = PostForm
    success_url = reverse_lazy("feeds__home")

    def form_valid(self, form):
        new_post = Post.objects.create(
            text=form.cleaned_data["text"], image=form.cleaned_data["image"]
        )
        return super().form_valid(form)
