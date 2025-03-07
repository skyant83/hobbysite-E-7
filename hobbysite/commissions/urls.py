from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('list/', CommissionListView.as_view(), name='list'),
    path('details<int:pk>/', CommissionDetailView.as_view(), name='comm-detail')
]

app_name = "commissions"