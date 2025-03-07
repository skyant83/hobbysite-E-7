from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "wiki/articles_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "wiki/article_detail.html"
