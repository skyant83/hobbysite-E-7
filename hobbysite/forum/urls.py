from django.urls import path

from .views import (ThreadListView,
                    ThreadDetailView,
                    ThreadCreateView,
                    ThreadUpdateView)

urlpatterns = [
    path('threads', ThreadListView.as_view(), name='thread_list'),
    path('thread/<int:pk>', ThreadDetailView.as_view(), name='thread_detail'),
    path('thread/add', ThreadCreateView.as_view(), name='thread_create'),
    path('thread/<int:pk>/edit',
         ThreadUpdateView.as_view(),
         name='thread_update'),
]

app_name = 'forum'
