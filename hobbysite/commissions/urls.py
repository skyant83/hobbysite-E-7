from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('list/', CommissionListView.as_view(), name='list'),
    path('details/<int:pk>', CommissionDetailView.as_view(), name='detail')
]

app_name = "commisions"
