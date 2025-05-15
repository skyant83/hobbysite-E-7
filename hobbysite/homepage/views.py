from django.shortcuts import render


def index(request):
    ctx = {
        'members': [
            'Badiola, Enrique Gabriel',
            'Dorde, Andre Benedict',
            'Pascual, Eizekiel Pierre',
            'Tabo, Ken Jonree',
            'Villegas, Jacob Noah',
        ]
    }
    return render(request, 'homepage/homepage.html', ctx)

# Create your views here.
