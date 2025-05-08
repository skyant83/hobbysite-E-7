from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "wiki/articles_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "wiki/article_detail.html"


class ArticleCreateView(CreateView):
    model = Article
    template_name = "wiki/article_create.html"


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "wiki/article_update.html"
