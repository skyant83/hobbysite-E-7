from django.shortcuts import render


def index(request):
    return render(request, 'homepage/homepage.html', context=None)

# Create your views here.
