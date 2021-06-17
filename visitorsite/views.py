from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models.posts import Post, Blog
from .models.embeds import Embed
from .forms import PostForm, EmbedForm


class BlogsListing(ListView):
    queryset = Blog.objects.filter(status=2).order_by('-created_on')
    model = Blog 


class SpecificBlogPostsListing(ListView):
    queryset = Post.objects.filter(status=2).order_by('-created_on')
    model = Post


class PostListing(ListView):
    queryset = Post.objects.filter(status=2).order_by('-created_on')
    model = Post 
    paginate_by = 3


class VideoPostListing(ListView):
    queryset = Post.objects.filter(status=2, cat=1).order_by('-created_on')
    model = Post 


class NewsPostListing(ListView):
    queryset = Post.objects.filter(status=2, cat=3).order_by('-created_on')
    model = Post 


class ImagePostListing(ListView):
    queryset = Post.objects.filter(status=2, cat=2).order_by('-created_on')
    model = Post 


class PostDetailsViewing(DetailView):
    model = Post


class PostCreating(CreateView):
    model = Post 
    form_class = PostForm


class PostUpdating(UpdateView):
    model = Post
    form_class = PostForm


class PostDeleting(DeleteView):
    model = Post
    success_url = reverse_lazy('blogs_listing_url')


#  -------------- Embeding -------------
class EmbedListing(ListView):
    queryset = Embed.objects.all()
    model = Embed 


class EmbedDetailsViewing(DetailView):
    model = Embed


class EmbedCreating(CreateView):
    model = Embed 
    form_class = EmbedForm


class EmbedUpdating(UpdateView):
    model = Embed
    form_class = EmbedForm


class EmbedDeleting(DeleteView):
    model = Embed
    success_url = reverse_lazy('blogs_listing_url')

