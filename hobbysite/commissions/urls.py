from django.urls import path
from .views import (
    CommissionListView, CommissionDetailView,
    CommissionCreateView, CommissionUpdateView
)

urlpatterns = [
    path('list/', CommissionListView.as_view(), name='list'),
    path('detail/<int:pk>', CommissionDetailView.as_view(), name='detail'),
    path('add', CommissionCreateView.as_view(), name='create'),
    path('<int:pk>/edit', CommissionUpdateView.as_view(), name='update'),
]

app_name = "commissions"
