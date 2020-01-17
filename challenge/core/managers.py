from django.db import models


class OnlyActiveManager(models.Manager):
    """Filter objects that are active."""

    def get_queryset(self):
        """Override the get_queryset to filter only active objects."""
        return super().get_queryset().filter(is_active=True)
