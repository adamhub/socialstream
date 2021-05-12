from django.contrib import admin
from visitorsite.models import Post

class PostsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostsAdmin)