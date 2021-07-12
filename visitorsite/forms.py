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
	honeypot = forms.CharField(required=False,label='If you enter anything in this field, your comment will be treated as spam')

	def clean_honeypot(self):
		"""Check that nothing's been entered into the honeypot."""
		value = self.cleaned_data["honeypot"]
		if value:
			raise forms.ValidationError("Oah, you're a bot..!")
		return value

	def save(self, commit=True):
		user = super(UserRegisterForm, self).save(commit=False)
		if commit:
			user.save()
		return user
	
	class Meta:
		model = User
		fields = ("username", "password1", "password2")
