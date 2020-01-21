from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext as _

from challenge.core.models import SoftDeleteModel, TimestampModel


class Book(SoftDeleteModel, TimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    author = models.ForeignKey('Author', on_delete=models.PROTECT)

    class Meta:
        db_table = 'book'
        verbose_name = _('Book')
        verbose_name_plural = _('Books')


class Category(SoftDeleteModel, TimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Author(SoftDeleteModel, TimestampModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'author'
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Review(SoftDeleteModel, TimestampModel):
    book = models.ForeignKey('Book', on_delete=models.PROTECT)
    description = models.TextField(verbose_name=_('Description'))
    evaluation = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')
