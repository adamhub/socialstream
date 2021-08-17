from django.db import models
from django.template.defaultfilters import truncatechars, truncatewords

from micawber import Cache, bootstrap_oembed

cache = Cache()  # Simple in-memory cache.
pr = bootstrap_oembed(cache=cache)

class Embed(models.Model):
    slug=models.CharField(max_length=500, verbose_name="slug")
    width=models.CharField(max_length=20, verbose_name="width", help_text="Only for link embeds(specify the width of embed code from ir's attributes)", blank=True,null=True, default=800)
    link=models.CharField(max_length=1500, verbose_name="Link Address of the Embed", help_text="example: https://youtube.com/something", blank=True,null=True)
    embed_code=models.TextField(max_length=10000, verbose_name="embed code", help_text="copy the embed code from your server and Past it here, if you use this field, the previous field will be ignored during template rendition", blank=True,null=True)
    description=models.TextField(max_length=10000, verbose_name="About this link/video", blank=True,null=True)
    
    def __str__(self): return self.slug
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('visitorsite:embed_viewing_url', args=[self.slug])

    @property
    def short_description(self):
        return truncatewords(self.description, 15)

    @property
    def short_embed_code(self):
        provider=self.embed_code.find("src")
        return self.embed_code[provider+13:150]

    @property
    def short_embed_link(self):
        try:
            provider=str(self.link).find("http")
            return self.link[provider+8:28]
        except:
            return None