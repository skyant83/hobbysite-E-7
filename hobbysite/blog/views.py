from django import forms
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView

from .forms import CommentForm
from user_management.models import Profile

from .models import Article, ArticleCategory, Comment

# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_articles = Article.objects.all()

        article_author = None
        if self.request.user.is_authenticated:
            article_author = Profile.objects.get(user=self.request.user)
            context['user_articles'] = all_articles.filter(
                author=article_author
            )

            all_articles.exclude(author=article_author)

            author_categories = {}
            for category in ArticleCategory.objects.all():
                author_categories[category] = (
                    Article.objects.filter(category=category) &
                    Article.objects.filter(author=article_author)
                )

            context['author_categories'] = author_categories

        categories = {}
        for category in ArticleCategory.objects.all():
            categories[category] = (
                Article.objects.filter(category=category) &
                Article.objects.exclude(author=article_author)
            )

        context['categories'] = categories

        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = Profile.objects.get(user=self.request.user)

        context['pk'] = self.kwargs['pk']
        author_articles = (
            Article.objects.exclude(pk=self.kwargs['pk']) &
            Article.objects.filter(author=self.get_object().author)
        )
        context['author_articles'] = author_articles

        context['form'] = CommentForm()
        context['comments'] = (
            Comment.objects.filter(article=context['object']) &
            Comment.objects.order_by('-created_on')
        )
        context['user'] = user

        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = Profile.objects.get(user=self.request.user)
            comment.article = Article.objects.get(pk=self.kwargs['pk'])
            comment.save()
            return redirect('blog:article', pk=self.kwargs['pk'])
        else:
            self.objects_list = self.get_queryset(**kwargs)
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'blog/article_create.html'
    fields = '__all__'

    def get_form(self, form_class=None):
        created_form = super().get_form(form_class)

        if self.request.user.is_authenticated:
            user = Profile.objects.get(user=self.request.user)
            created_form.fields['author'].initial = user
            created_form.fields['author'].disabled = True

        created_form.fields['header_image'].widget.attrs = {
            'style': 'color:transparent; width:90px;',
            'onchange': 'readURL(this)'
        }
        created_form.fields['title'].widget.attrs['style'] = 'width:100%'
        created_form.fields['entry'].widget.attrs['style'] = 'width:100%'
        created_form.instance.created_on = forms.DateTimeField()
        created_form.instance.created_on.initial = timezone.now()
        created_form.instance.updated_on = forms.DateTimeField(initial=timezone.now())
        return created_form


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'blog/article_update.html'
    fields = '__all__'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['author'].disabled = True
        form.fields['header_image'].widget.attrs['onchange'] = 'readURL(this);'
        form.fields['title'].widget.attrs['style'] = 'width:100%'
        form.fields['entry'].widget.attrs['style'] = 'width:100%'
        return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']
        return context
