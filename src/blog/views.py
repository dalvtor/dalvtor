from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.dates import MonthArchiveView
from . import models
from . import forms


class PostListView(ListView):
    model = models.Post
    context_object_name = 'latest_posts'
    paginate_by = 20

    def get_queryset(self):
        filters = forms.PostSearchForm(self.request.GET)
        query = filters.data.get('q', '')
        tag = filters.data.get('t')
        queryset = models.Post.objects.filter(
            title__icontains=query,
        ).prefetch_related('tags')

        if tag:
            return queryset.filter(tags__slug__iexact=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = models.Post.objects.all()
        context['tags'] = models.Tag.objects.all()
        return context


class PostArchiveView(PostListView, MonthArchiveView):
    queryset = models.Post.objects.all()
    date_field = "created_at"
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = models.Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
