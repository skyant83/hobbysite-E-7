from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Article

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_details.html'
