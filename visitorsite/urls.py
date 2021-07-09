from django.contrib.auth.decorators import login_required, permission_required
from django.urls import path
from django.views.generic import TemplateView
from .views import * # noqa


app_name="visitorsite"
urlpatterns = [

    path("accounts/signup/", SignUp.as_view(template_name="accounts/user_sign_up.html"), name="user_sign_up"),

    path('', PostListing.as_view(template_name="posts/posts.html"), name="posts_listing_url"),

    path('indexes/', IndexesListing.as_view(template_name="indexes/indexes.html"), name="indexes_url"),

    path('<get_parent_slug>/videos/', VideoPostListing.as_view(template_name="indexes/specific_posts.html"), name="specific_videos_posts_listing_url"),
    path('<get_parent_slug>/news/', NewsPostListing.as_view(template_name="indexes/specific_posts.html"), name="specific_news_posts_listing_url"),
    path('<get_parent_slug>/images/', ImagePostListing.as_view(template_name="indexes/specific_posts.html"), name="specific_images_posts_listing_url"),

    path('videos/', VideoPostListing.as_view(template_name="posts/posts.html"), name="public_videos_posts_listing_url"),
    path('news/', NewsPostListing.as_view(template_name="posts/posts.html"), name="public_news_posts_listing_url"),
    path('images/', ImagePostListing.as_view(template_name="posts/posts.html"), name="public_images_posts_listing_url"),

    path('create/', login_required(PostCreating.as_view(template_name="objects/create_or_update.html")), name="post_creating_url"),
    path('<slug>/update/', login_required(PostUpdating.as_view(template_name="objects/create_or_update.html")), name="post_updating_url"),
    path('<slug>/delete/', login_required(PostDeleting.as_view(template_name="objects/delete.html")), name="post_deleting_url"),
    path('<slug>/image/', PostDetailsViewing.as_view(template_name="posts/image.html"), name="image_viewing_url"),
    path('<slug>/', PostDetailsViewing.as_view(template_name='posts/post_details.html'), name="post_viewing_url"),

    path('embeds/', EmbedListing.as_view(template_name="embeds/embeds.html"), name="embeds_listing_url"),

    path('embeds/create/', login_required(EmbedCreating.as_view(template_name="objects/create_or_update.html")), name="embed_creating_url"),
    path('embeds/<slug>/update/', login_required(EmbedUpdating.as_view(template_name="objects/create_or_update.html")), name="embed_updating_url"),
    path('embeds/<slug>/delete/', login_required(EmbedDeleting.as_view(template_name="objects/delete.html")), name="embed_deleting_url"),
    path('embeds/<slug>/', EmbedDetailsViewing.as_view(template_name='embeds/embed_details.html'), name="embed_viewing_url"),

    path('indexes/<get_parent_slug>/', SpecificIndexPostsListing.as_view(template_name="indexes/specific_posts.html"), name="index_details_viewing_url"),
]
