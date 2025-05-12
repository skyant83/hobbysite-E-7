from django.views.generic import ListView, DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin

from user_management.models import Profile
from .models import Thread


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
            context["other_threads"] = Thread.objects.all() \
                                             .exclude(author=current_profile)
        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'
