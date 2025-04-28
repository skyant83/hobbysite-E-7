from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile


# Create your views here.
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['display_name', 'email_address']
    template_name = 'user_management/profile_detail.html'
