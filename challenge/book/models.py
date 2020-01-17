from django.db import models

from challenge.core.models import SoftDeleteModel, TimestampModel
from django.utils.translation import gettext as _


class Book(SoftDeleteModel, TimestampModel):
    book_cover = models.ImageField(verbose_name=_('Book Cover'))
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)
    review = models.ForeignKey('Review', on_delete=models.PROTECT)


class Category(SoftDeleteModel, TimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'))


class Author(SoftDeleteModel, TimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'))


class Review(SoftDeleteModel, TimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'))
