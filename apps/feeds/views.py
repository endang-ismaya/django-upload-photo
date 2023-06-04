from django.views.generic import TemplateView, DetailView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

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

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        Post.objects.create(
            text=form.cleaned_data["text"], image=form.cleaned_data["image"]
        )
        messages.add_message(
            self.request, messages.SUCCESS, "Your post successfully added."
        )
        return super().form_valid(form)
