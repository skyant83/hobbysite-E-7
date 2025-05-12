from django.shortcuts import redirect
from django.urls import reverse_lazy
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
            context['similar_threads'] = \
                Thread.objects.filter(category=self.get_object().category) \
                              .exclude(pk=self.get_object().pk)
            context['comments'] = \
                Comment.objects.filter(thread=self.get_object())
            context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = Profile.objects.get(user=self.request.user)
            comment.thread = self.get_object()
            comment.save()
            return redirect('forum:thread_detail', pk=self.kwargs['pk'])
        else:
            self.object = self.get_object()
            context = self.get_context_data(**kwargs)
            context['comment_form'] = comment_form
            return self.render_to_response(context)


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    fields = ['title', 'category', 'entry', 'image']
    template_name = 'forum/thread_create.html'

    def form_valid(self, form):
        form.instance.author = Profile.objects.get(user=self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('forum:thread_detail',
                            kwargs={'pk': self.kwargs['pk']})


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    fields = ['title', 'category', 'entry', 'image']
    template_name = 'forum/thread_edit.html'

    def get_success_url(self):
        return reverse_lazy('forum:thread_detail',
                            kwargs={'pk': self.kwargs['pk']})
