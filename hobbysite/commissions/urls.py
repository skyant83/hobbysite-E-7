from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('list/', CommissionListView.as_view(), name='list'),
    path('details/', CommissionDetailView.as_view(), name='comm_detail')
]

app_name = "commisions"