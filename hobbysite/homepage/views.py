from django.shortcuts import render


def index(request):
    ctx = {
        'members': [
            'Badiola, Enrique Gabriel',
            'Dorde, Andre Benedict',
            'Pascual, Eizekiel Pierre',
            'Tabo, Ken Jonree',
            'Villegas, Noah Jacob',
        ]
    }
    return render(request, 'homepage/homepage.html', ctx)

# Create your views here.
