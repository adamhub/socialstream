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



class Topic(Page):
    """ An Topic Page to list the specific Blogs/Posts/Entries """
    image = models.ImageField(upload_to='images/',verbose_name="Topic Header Image", blank=True, null=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('visitorsite:index_details_viewing_url', args=[self.slug])
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'


class Post(Page):
    """ A Post/Entry Page """
    image = models.ImageField(upload_to='images/',verbose_name="Internal Header Image", blank=True, null=True)
    external_image = models.CharField(verbose_name="External Header Image", max_length=150, blank=True, null=True,help_text="From external link")
    type = models.IntegerField(choices=((0,_("Standard Post Page")),(1,_("Video Post Page")),(2,_("Image Post Page")),(3,_("News Post Page"))), default=0)
    body = models.TextField(max_length=10000, verbose_name="Main content section ", blank=True)
    date_published = models.DateTimeField("Date article published", blank=True, null=True, auto_now_add=True)
    embed_file = models.ForeignKey(Embed,verbose_name=_('Embeded Video'),null=True,blank=True,
        editable=True,on_delete=models.SET_NULL,related_name='embeded_video',help_text="PLease select or create an embed object"
        )
    topic_page = models.ForeignKey(Topic,verbose_name=_('Post Topic'),null=True,blank=True,
        editable=True,on_delete=models.SET_NULL,related_name='posts',help_text="Topic Page that this post will be residing in it's listing"
        )

    def get_topic_listing_slug(self): return self.topic_page.slug
        
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
            ct=comment_model.objects.first().content_type.id
            return comment_model.objects.filter(content_type=ct, object_pk=self.pk, site__pk=1)[:3]
        except:
            print("none")
            return None

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
