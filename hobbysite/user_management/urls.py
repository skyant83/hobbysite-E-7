from django.urls import path

from .views import ProfileUpdateView, ProfileCreateView

urlpatterns = [
    path('<int:pk>',
         ProfileUpdateView.as_view(),
         name='profile_update'),
    path('registration',
         ProfileCreateView.as_view(),
         name='profile_create')
]

app_name = "user_management"
