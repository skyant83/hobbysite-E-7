from django.shortcuts import render
from .models import ArticleCategory, Article

def index(request):
    ctx = {
        "list_view_path": "wiki/articles",
        "categories_list": ArticleCategory.objects.all(),
        "articles_list": Article.objects.all(),
    }
    return render(request, "index.html", ctx)

def articles_list(request):
    all_articles = Article.objects.all()
    ctx = {"articles": all_articles if all_articles else []}
    return render(request, "articles_list.html", ctx)

def article_detail(request, pk):
    ctx = {"details": Article.objects.get(pk=pk)}
    return render(request, "article_detal.html", ctx)