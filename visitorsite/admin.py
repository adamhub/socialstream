from django.contrib import admin
from visitorsite.models import Post, Page, Index, Embed


@admin.register(Page)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Index)
class IndexesAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'status','blog_page','cat','created_on', 'embed_file')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Embed)
class EmbedsAdmin(admin.ModelAdmin):
    list_display = ('id','slug','short_embed_link', 'short_embed_code', 'short_description')
    list_filter = ("slug","id")
    search_fields = ['id', 'slug']

