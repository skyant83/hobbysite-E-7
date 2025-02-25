from django.urls import path
from .views import index, articles_list, article_detail
urlpatterns = [
    path("", index, name="index"),
    path("wiki/articles", articles_list, name="articles_list"),
    path("wiki/article/<int:pk>", article_detail, name="article_detail"),
]

app_name = "wiki"
