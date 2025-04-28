from django.urls import path
from .views import ProfileUpdateView

urlpatterns = [
    path('profile', ProfileUpdateView.as_view(), name='profile-update-view'),
]

app_name = "user_management"
