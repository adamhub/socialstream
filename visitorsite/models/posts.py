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




class Index(Page):
    """ An Index Page to list the specific Blogs/Posts/Entries """
    image = models.ImageField(upload_to='images/',verbose_name="Blog Pgae Header Image", blank=True, null=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('visitorsite:index_details_viewing_url', args=[self.slug])


class Post(Page):
    """ A Post/Entry Page """
    image = models.ImageField(upload_to='images/',verbose_name="Internal Header Image", blank=True, null=True)
    external_image = models.CharField(verbose_name="External Header Image", max_length=150, blank=True, null=True,help_text="From external link")
    cat = models.IntegerField(choices=((0,_("Standard Post Page")),(1,_("Video Post Page")),(2,_("Image Post Page")),(3,_("News Post Page"))), default=0)
    body = models.TextField(max_length=10000, verbose_name="Main content section ", blank=True)
    date_published = models.DateField("Date article published", blank=True, null=True)
    embed_file = models.ForeignKey(Embed,verbose_name=_('Embeded Video'),null=True,blank=True,
        editable=True,on_delete=models.SET_NULL,related_name='embeded_video',help_text="PLease select or create an embed object"
        )
    blog_page = models.ForeignKey(Index,verbose_name=_('Blog Page'),null=True,blank=True,
        editable=True,on_delete=models.SET_NULL,related_name='created_pages',help_text="Blog Page that this post will be residing in it's listing"
        )

    def get_parent_slug(self): return self.blog_page.slug
        
    def get_parent_object(self): return self.blog_page
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('visitorsite:post_viewing_url', args=[self.slug])
    
    def get_comment_form_target(self):
        """
        Returns the target URL for the comment form submission view.
        """
        from django.urls import reverse
        return reverse("comments_success_url" )

    def get_image_url(self):
        from django.urls import reverse
        return reverse('visitorsite:image_viewing_url', args=[self.slug])

    # get Author's Details of the post creator.
    def get_author_details(self):
        return Author.objects.filter(user=self.creator)
    
    def get_obj_latest_comments(self):
        try:
            import django_comments
            comment_model = django_comments.get_model()
            return comment_model.objects.filter(content_type=5, object_pk=self.pk, site__pk=1)
        except IndexError:
            return None
