from django.views.generic import ListView, DetailView

from .models import Thread


# Create your views here.
class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread.html'
