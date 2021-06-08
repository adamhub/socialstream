from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from django.views.generic import TemplateView
from .views import * # noqa


app_name="visitorsite"
urlpatterns = [

    path('', TemplateView.as_view(template_name="home_page.html"), name="home_page_url"),

    path('posts/', PostListing.as_view(template_name="posts/posts.html"), name="posts_listing_url"),

    path('blogs/', BlogsListing.as_view(template_name="blogs/blogs.html"), name="blogs_listing_url"),

    path('<get_parent_slug>/videos/', VideoPostListing.as_view(template_name="blogs/specific_posts.html"), name="specific_videos_posts_listing_url"),
    path('<get_parent_slug>/news/', NewsPostListing.as_view(template_name="blogs/specific_posts.html"), name="specific_news_posts_listing_url"),
    path('<get_parent_slug>/images/', ImagePostListing.as_view(template_name="blogs/specific_posts.html"), name="specific_images_posts_listing_url"),

    path('videos/', VideoPostListing.as_view(template_name="posts/posts.html"), name="public_videos_posts_listing_url"),
    path('news/', NewsPostListing.as_view(template_name="posts/posts.html"), name="public_news_posts_listing_url"),
    path('images/', ImagePostListing.as_view(template_name="posts/posts.html"), name="public_images_posts_listing_url"),

    path('posts/create/', login_required(PostCreating.as_view(template_name="objects/create_or_update.html")), name="post_creating_url"),
    path('posts/<slug>/update/', login_required(PostUpdating.as_view(template_name="objects/create_or_update.html")), name="post_updating_url"),
    path('posts/<slug>/delete/', login_required(PostDeleting.as_view(template_name="objects/delete.html")), name="post_deleting_url"),

    path('posts/<slug>/image/', PostDetailsViewing.as_view(template_name="posts/image.html"), name="image_viewing_url"),

    path('posts/<slug>/', PostDetailsViewing.as_view(template_name='posts/post_details.html'), name="post_viewing_url"),

    
    path('<get_parent_slug>/', SpecificBlogPostsListing.as_view(template_name="blogs/specific_posts.html"), name="blog_details_viewing_url"),
]
