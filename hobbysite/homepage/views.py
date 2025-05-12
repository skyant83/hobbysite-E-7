from django.shortcuts import render


def index(request):
    ctx = {
        'blog_link': ''
    }
    return render(request, 'homepage/homepage.html', ctx)

# Create your views here.
