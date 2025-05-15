from django import forms

from .models import Comment, Thread


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'category', 'entry', 'image']
        widgets = {'category': forms.Select()}
