from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('articles', index, name='articles'),
    path('article/<int:pk>', index, name='article'),
]

app_name = "blog"
