from django.views.generic import ListView, DetailView, DeleteView, CreateView

from .models.posts import Post
from .forms import PostForm


class PostListing(ListView):
    queryset = Post.objects.filter(status=2).order_by('-created_on')
    model = Post 


class VideoPostListing(ListView):
    queryset = Post.objects.filter(status=2, cat=1).order_by('-created_on')
    model = Post 


class NewsPostListing(ListView):
    queryset = Post.objects.filter(status=2, cat=3).order_by('-created_on')
    model = Post 


class ImagePostListing(ListView):
    queryset = Post.objects.filter(status=2, cat=2).order_by('-created_on')
    model = Post 


class PostViewing(DetailView):
    model = Post


class PostCreating(CreateView):
    model = Post 
    form_class = PostForm


class PostDeleting(DeleteView):
    model = Post
