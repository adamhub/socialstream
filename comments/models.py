from django.db import models
from django.utils.translation import gettext_lazy as _
from django_comments.abstracts import CommentAbstractModel

class CComment(CommentAbstractModel):
    user_email = models.EmailField(_("user's email address"), blank=True, null=True)
    