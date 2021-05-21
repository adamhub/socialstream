from django.contrib import admin
from visitorsite.models import Post, Page, Blog


class PagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Page, PagesAdmin)


class BlogsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title',]
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Blog, BlogsAdmin)


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'slug', 'status','blog_page','cat','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Post, PostsAdmin)
