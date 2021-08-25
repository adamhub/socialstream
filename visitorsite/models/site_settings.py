from django.db import models
from django.utils.translation import gettext_lazy as _


class Settings(models.Model):
    status = models.IntegerField(choices=((0,_("Active")),(1,_("Need to be Reviewed")),(2,_("InActive"))), default=0, help_text="only one of the active settings will be applied(the one that has lower id)")
    image = models.ImageField(upload_to='images/site_settings/',verbose_name="Logo", blank=True, null=True)

    def __str__(self):
        return f'{self.id} - {self.status} - {self.image.url}'
        
    class Meta:
        managed = True
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'