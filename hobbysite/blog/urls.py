from django.urls import path

from .views import ArticleDetailView, ArticleListView

urlpatterns = [
    path('articles', ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
]

app_name = "blog"
