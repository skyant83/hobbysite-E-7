from django.urls import path

from .views import ThreadListView, ThreadDetailView

urlpatterns = [
    path('threads', ThreadListView.as_view(), name='thread_list'),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='thread')
]

app_name = 'forum'
