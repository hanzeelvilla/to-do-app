from django import forms
from django.utils import timezone
from .models import Post

class PostForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Post
        fields = ['title', 'body', 'deadline']