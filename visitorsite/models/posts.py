from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from .pages import Page
from .embeds import Embed


class Author(models.Model):
    salutation = models.CharField(max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_('author'),null=True,blank=True,
        editable=True,on_delete=models.SET_NULL,related_name='published_posts'
        )
    headshot = models.ImageField(upload_to='authors_headshot')

    def __str__(self): return self.user




class Blog(Page):
    """ A Blog Page to list the specific Posts/Entries """
    image = models.ImageField(upload_to='images/',verbose_name="Blog Pgae Header Image", blank=True, null=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('visitorsite:blog_details_viewing_url', args=[self.slug])


class Post(Page):
    """ A Post/Entry Page """
    image = models.ImageField(upload_to='images/',verbose_name="Header Image", blank=True, null=True)
    cat = models.IntegerField(choices=((0,_("Standard Post Page")),(1,_("Video Post Page")),(2,_("Image Post Page")),(3,_("News Post Page"))), default=0)
    body = models.TextField(max_length=10000, verbose_name="Main content section ", blank=True)
    date_published = models.DateField("Date article published", blank=True, null=True)
    embed_file = models.ForeignKey(Embed,verbose_name=_('Embeded Video'),null=True,blank=True,
        editable=True,on_delete=models.SET_NULL,related_name='embeded_video',help_text="PLease select or create an embed object"
        )
    blog_page = models.ForeignKey(Blog,verbose_name=_('Blog Page'),null=True,blank=True,
        editable=True,on_delete=models.SET_NULL,related_name='created_pages',help_text="Blog Page that this post will be residing in it's listing"
        )

    def get_parent_slug(self): return self.blog_page.slug
        
    def get_parent_object(self): return self.blog_page
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('visitorsite:post_viewing_url', args=[self.slug])

    def get_image_url(self):
        from django.urls import reverse
        return reverse('visitorsite:image_viewing_url', args=[self.slug])

    # get Author's Details of the post creator.
    def get_author_details(self):
        return Author.objects.filter(user=self.creator)
