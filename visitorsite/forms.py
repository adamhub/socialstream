from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class UserRegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		if commit:
			user.save()
		return user