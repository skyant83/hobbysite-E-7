# <appname>/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('list/', index, name='list'),
    path('details/', index, name='comm-details')
]

app_name = "commisions"