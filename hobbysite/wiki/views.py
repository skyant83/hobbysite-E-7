from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from user_management.models import Profile
from .models import Article, Comment
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
        ctx['same_cat_articles'] = Article.objects.filter(
            category=curr_article.category) & Article.objects.exclude(
            pk=self.kwargs['pk'])
        return ctx

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Profile.objects.get(user=self.request.user)
            comment.article = Article.objects.get(pk=self.kwargs['pk'])
            comment.save()
            return self.get(request, *args, **kwargs)


class ArticleListView(ListView):
    model = Article
    template_name = 'wiki/articles_list.html'


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
