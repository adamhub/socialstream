from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Page(models.Model):
    title=models.CharField(verbose_name="Page Title", max_length=250)
    slug = models.SlugField(verbose_name=_('slug'), allow_unicode=True, max_length=255,
        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/")
        )
    status = models.IntegerField(choices=((0,_("Draft")),(1,_("UnPublished")),(2,_("Published"))), default=0)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name=_('creator'),null=True,blank=True,
        editable=True,on_delete=models.SET_NULL,related_name='created_pages'
        )
    seo_title = models.CharField(verbose_name=_("SEO title tag"),max_length=255,blank=True,
        help_text=_("The name of the page displayed on search engine results as the clickable headline.")
        )
    seo_description = models.TextField(verbose_name=_('SEO meta description'),blank=True,
        help_text=_("The descriptive text displayed underneath a headline in search engine results.")
        )
    created_on = models.DateTimeField(verbose_name=_('Created On'),blank=True,null=True,db_index=True,editable=False,auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name=_('Updated On'),auto_now= True)

    def __str__(self): return self.title
    
    def get_template(self, request, *args, **kwargs):
        if request.is_ajax():
            return self.ajax_template or self.template
        else:
            return self.template

    class Meta:
        ordering = ['-created_on']
