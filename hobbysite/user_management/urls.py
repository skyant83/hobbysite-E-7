from django.urls import path

from .views import ProfileUpdateView, ProfileCreateView

urlpatterns = [
    path('registration',
         ProfileCreateView.as_view(),
         name='profile_create'),
    path('<slug:slug>',
         ProfileUpdateView.as_view(),
         name='profile_update'),
]

app_name = "user_management"
