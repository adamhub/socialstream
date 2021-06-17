from django import forms

from .models.posts import Post
from .models.embeds import Embed


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ()


class EmbedForm(forms.ModelForm):
    class Meta:
        model = Embed
        exclude = ()