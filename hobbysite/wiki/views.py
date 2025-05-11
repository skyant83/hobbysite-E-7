from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from user_management.models import Profile
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'wiki/article_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticleDetailView, self).get_context_data(**kwargs)
        curr_article = ctx['object']

        ctx['pk'] = self.kwargs['pk']
        ctx['form'] = CommentForm()
        ctx['comments'] = Comment.objects.filter(article=curr_article)
        ctx['same_cat_articles'] = (
            Article.objects.filter(category=curr_article.category)
            & Article.objects.exclude(pk=self.kwargs['pk'])
        )
        return ctx

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Profile.objects.get(user=self.request.user)
            comment.article = Article.objects.get(pk=self.kwargs['pk'])
            comment.save()
            return redirect('wiki:article_detail', pk=self.kwargs['pk'])
        else:
            self.object_list = self.get_queryset(**kwargs)
            ctx = self.get_context_data(**kwargs)
            return self.render_to_response(ctx)


class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/articles_list.html'

    def get_context_data(self, **kwargs):
        ctx = super(ArticleListView, self).get_context_data(**kwargs)

        article_author = None
        if self.request.user.is_authenticated:
            article_author = Profile.objects.get(user=self.request.user)
            user_articles = Article.objects.filter(author=article_author)
            ctx['user_articles'] = user_articles

        categories = {}
        for category in ArticleCategory.objects.all():
            categories[category] = (
                Article.objects.filter(category=category)
                & Article.objects.exclude(author=article_author)
            )

        ctx['categories'] = categories
        return ctx


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'wiki/article_create.html'

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'wiki/article_update.html'
