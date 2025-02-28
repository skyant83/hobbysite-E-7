from django.views.generic import ListView, DetailView

from .models import Post


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'forum/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'forum/post.html'