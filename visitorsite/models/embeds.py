from django.db import models

class Embed(models.Model):
    link=models.CharField(max_length=1500, verbose_name="Link Address of the Video", help_text="example: https://youtube.com/something", blank=True,null=True)
    embed_code=models.TextField(max_length=10000, verbose_name="embeded code", help_text="copy the mbed code from your server and Past it here, if you use this field, the previous field will be ignored during template rendition", blank=True,null=True)
    description=models.TextField(max_length=10000, verbose_name="About this link/video", blank=True,null=True)