from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = [
    'AutoCreatedAtModel',
    'AutoUpdateAtModel',
    'AutoTimestampModel',
]


class AutoCreatedAtModel(models.Model):
    """ auto set created datetime """

    created_at = models.DateTimeField(
        verbose_name=_('created at'),
        auto_now_add=True,
        editable=False,
        null=True,
        blank=True)

    class Meta:
        abstract = True


class AutoUpdateAtModel(models.Model):
    """ auto set updated datetime """

    updated_at = models.DateTimeField(
        verbose_name=_('updated at'),
        auto_now=True,
        editable=False,
        null=True,
        blank=True)

    class Meta:
        abstract = True


class AutoTimestampModel(AutoCreatedAtModel, AutoUpdateAtModel):
    """ auto set created/updated datetime """

    class Meta:
        abstract = True
