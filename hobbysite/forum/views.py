from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from user_management.models import Profile
from .models import Thread, Comment
from .forms import CommentForm


# Create your views here.
class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            current_profile = Profile.objects.get(user=self.request.user)
            context["my_threads"] = \
                Thread.objects.filter(author=current_profile)
            context["other_threads"] = \
                Thread.objects.all() \
                              .exclude(author=current_profile)
        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["similar_threads"] = \
                Thread.objects.filter(category=self.get_object().category)
            context["comments"] = \
                Comment.objects.filter(thread=self.get_object())
        return context

    def post(self, request, *args, **kwargs):
        comment = CommentForm(request.POST)
        if comment.is_valid():
            comment.save(commit=False)
            comment.author = Profile.objects.get(user=self.request.user)
            comment.article = self.get_object()
            comment.save()
            return self.get(request, *args, **kwargs)
        else:
            self.object = self.get(**kwargs)
            context = self.get_context_data(**kwargs)
            context['comment_form'] = comment
            return self.render_to_response(context)


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title', 'category', 'entry', 'image']
    template_name = 'forum/thread_create.html'


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    fields = ['title', 'category', 'entry', 'image']
    template_name = 'forum/thread_edit.html'
