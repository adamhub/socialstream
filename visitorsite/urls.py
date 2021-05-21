from django.urls import path
from django.views.generic import TemplateView
from .views import PostListing, PostViewing, PostCreating, PostDeleting, VideoPostListing, NewsPostListing, ImagePostListing


app_name="visitorsite"
urlpatterns = [
    path('posts/', PostListing.as_view(template_name="posts/blog_page.html"), name="posts_listing"),
    path('videos/', VideoPostListing.as_view(template_name="posts/blog_page.html"), name="videos_posts_listing"),
    path('news/', NewsPostListing.as_view(template_name="posts/blog_page.html"), name="news_posts_listing"),
    path('images/', ImagePostListing.as_view(template_name="posts/blog_page.html"), name="imagesposts_listing"),
    path('posts/create/', PostCreating.as_view(template_name="objects/create.html"), name="post_creating"),
    path('posts/delete/<slug>/', PostDeleting.as_view(template_name="objects/delete.html"), name="post_deleting"),
    path('posts/<slug>/', PostViewing.as_view(template_name='posts/post_details.html'), name="post_viewing"),
    path('posts/<slug>/image/', PostViewing.as_view(template_name="posts/image.html"), name="image_viewing"),
]