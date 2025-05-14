from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    display_name = forms.CharField(max_length=63)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
