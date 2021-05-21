from django import forms
from .models import * # noqa

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()