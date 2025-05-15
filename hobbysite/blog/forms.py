from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    entry = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Add a comment...',
                'rows': 1,
            }
        ),
    )

    class Meta:
        model = Comment
        fields = ('entry',)
