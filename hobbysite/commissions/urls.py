# <appname>/urls.py
from django.urls import path
from .views import CommissionListView, CommissionDetailView

urlpatterns = [
    path('list/', CommissionListView.as_view(), name='list'),
    path('details/', CommissionDetailView.as_view(), name='comm-details')
]

app_name = "commisions"