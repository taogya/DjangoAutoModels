from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _

__all__ = [
    'AutoIDModel',
    'AutoBigIDModel',
    'AutoUUIDModel',
]


class AutoIDModel(models.Model):
    """ explicit declaration with AutoField """

    id = models.AutoField(
        verbose_name=_('ID'),
        editable=False,
        serialize=False,
        primary_key=True)

    class Meta:
        abstract = True


class AutoBigIDModel(models.Model):
    """ explicit declaration with BigAutoField """

    id = models.BigAutoField(
        verbose_name=_('ID'),
        editable=False,
        serialize=False,
        primary_key=True)

    class Meta:
        abstract = True


class AutoUUIDModel(models.Model):
    """ swap id from (Big)AutoFiled to UUIDField """

    id = models.UUIDField(
        verbose_name=_('UUID'),
        editable=False,
        serialize=False,
        primary_key=True,
        default=uuid4)

    class Meta:
        abstract = True
