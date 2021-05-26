from django.contrib import admin
from visitorsite.models import Post, Page, Blog, Embed


@admin.register(Page)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Blog)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'status','blog_page','cat','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Embed)
class EmbedsAdmin(admin.ModelAdmin):
    list_display = ('id','link', 'description')

