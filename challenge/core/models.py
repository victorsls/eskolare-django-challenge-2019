from django.db import models

from challenge.core.managers import OnlyActiveManager


class SoftDeleteModel(models.Model):
    is_active = models.BooleanField(default=True)
    objects = OnlyActiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        """Override the delete method, inactivating object."""
        if self.is_active:
            self.is_active = False
            super().save(update_fields=['is_active'])


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
