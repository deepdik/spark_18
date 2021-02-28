import datetime

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _


class TokenPool(models.Model):
    """
	"""
    token = models.CharField(_('token'), max_length=200, unique=True)
    is_assigned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expire_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'token_pool'
        permissions = ()

    def __str__(self):
        return str(self.id)